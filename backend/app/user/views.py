from django.shortcuts import render

# Create your views here.


from user.models import *
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
#from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import  permission_classes , api_view ,renderer_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.exceptions import PermissionDenied
from rest_framework.authtoken.models import Token
import string,random

class UserViewSet(APIView):
    @api_view(['GET'])  
    @permission_classes([IsAuthenticated])
    def getUserInfo(request):
        userdetail = UserDetail.objects.get(user=request.user)
        ret = {}
        ret['created_date'] = userdetail.created_date
        ret['username'] = request.user.username
        ret['email'] = request.user.email
        return Response(ret)


class RegisterViewSet(APIView):
    @api_view(['POST'])
    def register(request):
        if (not ('email' in request.data and 'username' in request.data)) or (request.data['email'] == "" or request.data['username'] == ""):
            raise PermissionDenied({"message":"Missing args."})
        email = request.data['email'] #{"email":"something@a.edu","username":"test"}
        username = request.data['username']
         
        # 找是否存在
        try :
            isEmail = User.objects.get(email__exact=email)
        except:
            isEmail = None
        if  isEmail:
            raise PermissionDenied({"message":"Email has benn used"})
        try:
            isUser = UnverifyUser.objects.get(username=username)
        except:
            isUser = None
        if  isUser :
            raise PermissionDenied({"message":"Username has been used"})

        token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40))
        new_user = UnverifyUser(
            username= request.data['username'],
            email = email,
            token = token,
            ).save()
        msg = 'Please copy the token to the apps: ' +  token + "\n" +"or click the link below " + request.build_absolute_uri('/')[:-1].strip("/") + "/#/register_next/"  + token
        send_mail('Confirm mail', msg, 'foxo.demo.verify@foxo.tw', [email])
        return Response({"message":"A EMAIL has been sent"})
    @api_view(['POST'])
    def confirm(request):
        try:
            user = UnverifyUser.objects.get(token=request.data['token'])#{"token":"6JZ5Y7CQW0YWETECTMU2AOCGRP8YXUOD3DOU4QM8"}
        except:
            raise PermissionDenied({"message":"Invalid token."})
        return Response({"username":user.username,"email":user.email})
    @api_view(['POST'])
    def createUser(request):#{"token":"8WGD7XYVKEBWQTSIX18YVHCYDQJOK09ITX3HY8B4","password":"test","sex":"male"}
        if not ('password' in request.data):
            raise PermissionDenied({"message":"Hacker:("})
        try:
            pre_user = UnverifyUser.objects.get(token=request.data['token'])
        except :
            raise PermissionDenied({"message":"Invalid token."})
        if  not pre_user.isCreate:
            new_user = User.objects.create_user(
                pre_user.username,
                pre_user.email, 
                request.data['password']
                )
            pre_user.isCreate = True
            new_user_detail = UserDetail(
                user = new_user,
            )
            # save at last
            new_user_detail.save()
            pre_user.save()
            new_user.save()
            token = Token.objects.create(user=new_user).key
            return Response({"username":new_user.username,"token":token})
        else:
            raise PermissionDenied({"message":"User has been create"})
        

