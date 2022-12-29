from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import  permission_classes , api_view ,renderer_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.exceptions import PermissionDenied,ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from androguard.core.bytecodes.apk import APK
from app.models import *
from app.serializers import *
from app.lib import *
from django.conf import settings
from zipfile import ZipFile
import time
RET_TEMPLATE = {
    'status': 500,
    'msg': "Not INIT",
    'data':None
}

class ListTask(APIView):
    @api_view(['GET'])
    def list(request):
        ret = RET_TEMPLATE.copy()
        pub_app = APPDetail.objects.filter(isPublic=True,status__gte=100)#dont list not finish    
        
        data ={} 
        if request.user.is_authenticated:
            self_app = APPDetail.objects.filter(owner=request.user)    
            data['self'] =  APPDetailSerializer(self_app,many=True).data
        data['pub'] = APPDetailSerializer(pub_app,many=True).data

        for dtype in data:
            for app in data[dtype]:
                app['tags']  = [x.data for x in APPLog.objects.filter(app_id=app['app_id'],type="tags")]
        ret['status'] = 200  
        ret['msg'] = data
        return Response(ret) 
class FileUploadView(APIView):
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def new(request):
        if not 'file' in request.FILES or not 'feature' in request.data :
            raise ValidationError({"message":"No file"})
        my_file = request.FILES['file']
        flag = 0
        while True:
            flag +=1
            uuid = id_generator()
            if not APPDetail.objects.filter(uuid=uuid).exists():
                break
            if flag > 50:
                raise ValidationError({"message":"UUID fail"})

        temp_file_name = '/tmp/'+uuid
        with open(temp_file_name, 'wb+') as temp_file:
            for chunk in my_file.chunks():
                temp_file.write(chunk)
        try:
            apk = APK(temp_file_name)
        except:
            raise ValidationError({"message":"Not A APK"})
        #insert db
        app_insert = APPDetail(
                name = apk.get_package(),
                md5  = md5(temp_file_name),
                size = os.stat(temp_file_name).st_size,
                androidversion_name = apk.get_androidversion_name() if  apk.get_androidversion_name() else "" ,
                uuid = uuid,
                owner = request.user,
                app_displayname = apk.get_app_name(),
                hook_feature = request.data['feature'],
            )          
        app_insert.save()
        try:
        # export icon
            with ZipFile(temp_file_name, 'r') as zipObj:
                source = zipObj.open(apk.get_app_icon())
                target = open(settings.UPLOAD_BASE + "icon/" + uuid + ".png", "wb")
                with source, target:
                    shutil.copyfileobj(source, target)
        except:
            pass
                        
        #move apk file
        shutil.move(temp_file_name, settings.UPLOAD_BASE + "apk/" + uuid + ".apk")
        return Response({
            "status":200,
            "id" :app_insert.app_id,
            })

class APPTaskView(APIView):
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def status(requests,app_id):
        ret = RET_TEMPLATE.copy()
        try:
            app = APPDetail.objects.get(pk=int(app_id))
        except:
            raise PermissionDenied(ret)
        if ((not app.isPublic) and 
            request.user != app.owner and  
            not request.user.is_superuser):
            ret['status'] = 401
            ret['msg'] = "PermissionDenied"
            raise PermissionDenied(ret)
        if app.job_start_time and int(app.job_start_time.strftime('%s')) +app.job_alive_time<time.time():
            app.status = 999
            app.save()
        ret['status'] = 200
        ret['msg'] = APPDetailSerializer(app).data
        return Response(ret)
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def addtime(requests,app_id):
        ret = RET_TEMPLATE.copy()
        app = APPDetail.objects.get(pk=int(app_id))
        if ((not app.isPublic) and 
            request.user != app.owner and  
            not request.user.is_superuser):
            ret['status'] = 401
            ret['msg'] = "PermissionDenied"
            raise PermissionDenied(ret)
        if ( app.job_alive_time > 500 ):
            ret['status'] = 400
            ret['msg'] = "超過上限"
            return Response(ret)
        app.job_alive_time += 30
        app.save()
        ret['status'] = 200  
        ret['msg'] = APPDetailSerializer(app).data
        return Response(ret)
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def stop(requests,app_id):
        ret = RET_TEMPLATE.copy()
        app = APPDetail.objects.get(pk=int(app_id))
        if ((not app.isPublic) and 
            request.user != app.owner and  
            not request.user.is_superuser):
            ret['status'] = 401
            ret['msg'] = "PermissionDenied"
            raise PermissionDenied(ret)
        app.job_alive_time = 0
        app.save()
        ret['status'] = 200  
        ret['msg'] = APPDetailSerializer(app).data
        return Response(ret)
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def getlog(requests,app_id):
        ret = RET_TEMPLATE.copy()
        app = APPDetail.objects.get(pk=int(app_id))
        if ((not app.isPublic) and 
            request.user != app.owner and  
            not request.user.is_superuser):
            ret['status'] = 401
            ret['msg'] = "PermissionDenied"
            raise PermissionDenied(ret)
        
        logs = APPLog.objects.filter(app_id=app)      
        ret['status'] = 200  
        ret['msg'] = APPLogSerializer(logs,many=True).data
        return Response(ret)
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def getscreenshot(requests,app_id):
        ret = RET_TEMPLATE.copy()
        app = APPDetail.objects.get(pk=int(app_id))
        if ((not app.isPublic) and 
            request.user != app.owner and  
            not request.user.is_superuser):
            ret['status'] = 401
            ret['msg'] = "PermissionDenied"
            raise PermissionDenied(ret)
        
        logs = APPScreenShot.objects.filter(app_id=app)      
        ret['status'] = 200  
        ret['msg'] = APPScreenShotSerializer(logs,many=True).data
        return Response(ret)
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def restart(requests,app_id):
        ret = RET_TEMPLATE.copy()
        app = APPDetail.objects.get(pk=int(app_id))
        if ((not app.isPublic) and 
            request.user != app.owner and  
            not request.user.is_superuser):
            ret['status'] = 401
            ret['msg'] = "PermissionDenied"
            raise PermissionDenied(ret)
        
        app.status = APPStatus.FRIDA_RESTART 
        app.save()    
        ret['status'] = 200  
        ret['msg'] = "Success"
        return Response(ret)
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def rerun(request,app_id):
        ret = RET_TEMPLATE.copy()
        app = APPDetail.objects.get(pk=int(app_id))
        if ((not app.isPublic) and 
            request.user != app.owner and  
            not request.user.is_superuser):
            ret['status'] = 401
            ret['msg'] = "PermissionDenied"
            raise PermissionDenied(ret)
        
        app_insert = APPDetail(
                name = app.name,
                md5  = app.md5,
                size = app.size,
                androidversion_name = app.androidversion_name,
                uuid =  app.uuid,
                owner = request.user,
                app_displayname = app.app_displayname,
                hook_feature = app.hook_feature,
            )          
        app_insert.save()
        ret['status'] = 200  
        ret['msg'] = "Success"
        ret["id"] = app_insert.app_id
        return Response(ret)