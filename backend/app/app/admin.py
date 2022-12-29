from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(APPDetail)
admin.site.register(APPLog)
admin.site.register(APPScreenShot)
