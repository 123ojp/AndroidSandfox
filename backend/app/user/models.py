from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.

class UserDetail(models.Model):
    user = models.OneToOneField(User,
            on_delete=models.CASCADE, related_name='profile')
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user)

class UnverifyUser(models.Model):
    username = models.CharField(unique=True,max_length=30)
    email = models.EmailField()
    token = models.CharField(unique=True,max_length=40)
    isCreate = models.BooleanField(default=False)

    def __str__(self):
        return self.username
