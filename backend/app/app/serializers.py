from app.models import *

from rest_framework import serializers

class APPDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APPDetail
        fields = [ 'app_id',
        'name','md5','size','hook_feature',
        'androidversion_name','uuid','app_displayname',
        'status','created_date','job_alive_time','job_start_time','last_worker_time','status_msg',
        'scrcpy_url'] 

class APPLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APPLog
        fields = ( 'id',
        'type','created_date','dataWtype')

class APPScreenShotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APPScreenShot
        fields = ( 'id',
        'path','created_date')