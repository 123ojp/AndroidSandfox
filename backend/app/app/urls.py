from django.urls import path
from app import views
from rest_framework.authtoken.views import obtain_auth_token  # rest login
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
urlpatterns = [
    path('new', views.FileUploadView.new),
    path('list', views.ListTask.list),
    path('<str:app_id>/status',views.APPTaskView.status),
    path('<str:app_id>/addtime',views.APPTaskView.addtime),
    path('<str:app_id>/stop',views.APPTaskView.stop),
    path('<str:app_id>/log',views.APPTaskView.getlog),
    path('<str:app_id>/screen',views.APPTaskView.getscreenshot),
    path('<str:app_id>/restart',views.APPTaskView.restart),
    path('<str:app_id>/rerun',views.APPTaskView.rerun),

]+ static('uploads', document_root=settings.UPLOAD_BASE)