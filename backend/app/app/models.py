from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import json
class APPStatus:
    INIT = 0
    WORKER_GOT = 1
    ALLOCATE = 2
    START = 3
    FRIDA_RESTART = 4
    FINISH = 100
    FAIL = 999
    

# Create your models here.
class APPDetail(models.Model):
    app_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    app_displayname = models.CharField(max_length=200,default="")
    md5 = models.CharField(max_length=40)
    size = models.IntegerField()
    androidversion_name = models.CharField(max_length=40,default="")
    uuid = models.CharField(max_length=40)
    owner =  models.ForeignKey(User,
        on_delete=models.CASCADE)
    status = models.IntegerField(default=0) #0 not start 1 start 2 end
    status_msg = models.CharField(max_length=200,null=True,default="Allocating To Worker")
    created_date = models.DateTimeField(default=timezone.now)
    scrcpy_url = models.CharField(max_length=200,null=True)
    last_worker_time = models.DateTimeField(null=True,blank=True)
    worker_uuid = models.CharField(max_length=200,null=True)
    job_start_time = models.DateTimeField(null=True,blank=True)
    job_alive_time = models.IntegerField(default=300)
    isPublic = models.BooleanField(default=True)
    hook_feature = models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.name)

class APPLog(models.Model):
    app_id = models.ForeignKey(APPDetail,
        on_delete=models.CASCADE)
    type = models.CharField(max_length=40)
    data =  models.CharField(max_length=40000)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.app_id.app_id) +" - "+ str(self.app_id )+ ' - ' + self.type
    def dataWtype(self):
        return {
            'type':self.type,
            'data':json.loads(self.data)
        }
class APPScreenShot(models.Model):
    app_id = models.ForeignKey(APPDetail,
        on_delete=models.CASCADE)
    path =  models.CharField(max_length=40)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.app_id.app_id) +" - "+ str(self.app_id )+ ' - ' + self.path
 