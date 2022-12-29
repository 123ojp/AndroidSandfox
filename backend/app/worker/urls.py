from django.urls import path
from worker import views
from rest_framework.authtoken.views import obtain_auth_token  # rest login
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
urlpatterns = [
    path('getjob/<str:worker_uuid>', views.JobView.new),
    path('confirmjob/<str:worker_uuid>/<str:app_id>', views.JobView.dojob),
    path('<str:app_id>/log', views.LogView.new), 
    path('<str:uuid>/getapk', views.JobView.getapk),
    path('<str:app_id>/status', views.JobView.status),
    path('<str:app_id>/update', views.JobView.update),
    path('<str:app_id>/screenshot', views.ScreenshotUploadView.new),

] + static('uploads', document_root=settings.UPLOAD_BASE)