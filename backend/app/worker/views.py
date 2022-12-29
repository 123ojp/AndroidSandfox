from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import  permission_classes , api_view ,renderer_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.timezone import utc
from app.lib import *
from app.serializers import *
from app.models import *
from worker.models import *
from django.conf import settings

import json
# Create your views here.
RET_TEMPLATE = {
    'status': 500,
    'msg': "Not INIT",
    'type':WorkerJobStatus.NOJOB
}


class JobView(APIView):
    @api_view(['GET'])
    def new(request,worker_uuid):
        ret = RET_TEMPLATE.copy()
        app_list = APPDetail.objects.filter(status__lte=APPStatus.WORKER_GOT).order_by('created_date')
        for app in app_list:
            if app.status == APPStatus.WORKER_GOT and (datetime.utcnow().replace(tzinfo=utc) - app.last_worker_time).total_seconds()  < 5:
                continue #not timeout
            app.status = APPStatus.WORKER_GOT
            app.last_worker_time =  datetime.now()
            app.worker_uuid = worker_uuid
            app.save()
            ret['status'] = 200
            ret['type'] = WorkerJobStatus.NEWJOB
            ret['msg'] = APPDetailSerializer(app).data
            return Response(ret)
        ret['status'] = 200
        ret['msg'] = "No job Now"
        ret['type'] = WorkerJobStatus.NOJOB
        return Response(ret)
    @api_view(['GET'])
    def dojob(request,worker_uuid,app_id):
        ret = RET_TEMPLATE.copy()
        app = APPDetail.objects.get(pk=int(app_id))
        if app and app.status == APPStatus.WORKER_GOT and app.worker_uuid == worker_uuid:
            app.status = APPStatus.ALLOCATE
            app.job_start_time =  datetime.now()
            app.save()
            ret['status'] = 200
            ret['type'] = WorkerJobStatus.ALLOCATE_JOB
            ret['msg'] = "Allocate Job "+app_id+" to workerID "+ worker_uuid
        else :
            ret['status'] = 400
            ret['type'] = WorkerJobStatus.NO_PERMISSION
            ret['msg'] = "Worker uuid not match"
        return Response(ret)
    @api_view(['GET'])
    def status(request,app_id):
        ret = RET_TEMPLATE.copy()
        app = APPDetail.objects.get(pk=int(app_id))
        ret['status'] = 200
        ret['type'] = 0
        ret['msg'] = APPDetailSerializer(app).data
        return Response(ret)
    @api_view(['POST'])
    def update(request,app_id): #todo   
        ret = RET_TEMPLATE.copy()
        app = APPDetail.objects.get(pk=int(app_id))
        job_start_time = request.data.get('job_start_time',None)
        
        if job_start_time:
            app.job_start_time =  datetime.now()
        status = request.data.get('status',None)
        if status != None:
            app.status = status
        scrcpy_url = request.data.get('scrcpy_url',None)
        if scrcpy_url:
            app.scrcpy_url = scrcpy_url
        status_msg = request.data.get('status_msg',None)
        if status_msg:
            app.status_msg = status_msg
        app.save()
        ret['status'] = 200
        ret['type'] = 0
        ret['msg'] = APPDetailSerializer(app).data
        return Response(ret)
    @api_view(['GET'])
    def getapk(request,app_id): #todo   
        return Response(200)
class LogView(APIView):
    @api_view(['POST'])
    def new(request,app_id):
        ret = RET_TEMPLATE.copy()
        app = APPDetail.objects.get(pk=int(app_id))
        if (app.status != APPStatus.START):
            ret['status'] = 400
            ret['msg'] = "Task not started"
            return Response(ret)
        type = request.data.get('type')
        data = request.data.get('data')
        if type =='tags':
            if APPLog.objects.filter(app_id = app_id,data=json.dumps(data)).exists():
                ret['status'] = 400
                ret['msg'] = "Same Tags"
                return Response(ret)
        newlog = APPLog(
            app_id = APPDetail.objects.get(app_id = app_id),
            type = type,
            data = json.dumps(data),
        )
        newlog.save()
        ret['status'] = 200
        ret['type'] = 0
        ret['msg'] = newlog.id
        ret['debug'] = request.data.get('data')
        return Response(ret)
        
    

class ScreenshotUploadView(APIView):
    @api_view(['POST'])
    def new(request,app_id):
        if not 'file' in request.FILES:
            raise PermissionDenied({"message":"No file"})
        my_file = request.FILES['file']
        flag = 0
        while True:
            flag +=1
            uuid = id_generator()+'.png'
            if not APPScreenShot.objects.filter(path=uuid).exists():
                break
            if flag > 50:
                raise PermissionDenied({"message":"UUID fail"})

        temp_file_name = '/tmp/'+uuid
        with open(temp_file_name, 'wb+') as temp_file:
            for chunk in my_file.chunks():
                temp_file.write(chunk)
        
        #insert db
        app_insert = APPScreenShot(
                app_id = APPDetail.objects.get(pk=int(app_id)),
                path = uuid,
            )          
        app_insert.save()

        #move apk file
        shutil.move(temp_file_name, settings.UPLOAD_BASE + "screenshot/" + uuid)

        return Response({
            "status":200,
            "id" :app_insert.app_id.app_id,
            })