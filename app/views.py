from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.sessions.models import Session
from app import models

import json


# Create your views here.

#   功能模块：
# 1、Login       用户登录
# 2、toIndex     用户注册
# 3、LoginOut    用户登出
#

# ========================
# 1、用户登录
# ========================
def Login(request):
    data = {'status': 0}
    if request.method == 'POST':
        receive_data = json.loads(request.body)
        print(receive_data)
        userName = receive_data['username']
        password = receive_data['password']
        get_user = models.UserInfor.objects.get(userName=userName)  # 获取数据库数据
        if get_user:
            if (get_user.userName == userName and check_password(password,
                                                                 get_user.password)):  # 采用MD5进行密码加密。所以使用check_password方式进行密码检验
                data['status'] = 1
                print(model_to_dict(get_user))
                request.session['userInfor'] = model_to_dict(get_user)
        print('=======')
    return HttpResponse(json.dumps(data), content_type='application/json')  # 把数据以json格式返回给前台ajax


# ========================
# 2、用户注册
# ========================
def Register(request):
    data = {'status': 0}
    if request.method == 'POST':
        receive_data = json.loads(request.body)
        isExit = models.UserInfor.objects.filter(userName=receive_data['username'])
        if isExit:
            pass
        else:
            new_user = models.UserInfor(
                userName=receive_data['username'],
                password=make_password(receive_data['password']),
                position='1',
                workId=models.UserInfor.objects.count()
            )
            try:
                new_user.save()
                data['status'] = 1
            except:
                pass
    return HttpResponse(json.dumps(data), content_type='application/json')


# ========================
# 3、用户登出
# ========================
def LoginOut(request):
    key = request.session.session_key
    Session.objects.filter(session_key=key).delete()
    return redirect('/')
