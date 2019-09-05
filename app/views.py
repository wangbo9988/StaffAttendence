from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.sessions.models import Session
from django.db import connection

from app import models

import datetime
import json
import uuid


# Create your views here.

#   功能模块：
# 1、Login           用户登录
# 2、toIndex         用户注册
# 3、LoginOut        用户登出
# 4、GetUserInfor    获取用户信息
# 5、PunchIn         员工打卡
# 6、ChangeUserInfor 修改员工信息
# 7、ApplyLeave      申请休假
#

# ========================
# 1、用户登录
# ========================
def Login(request):
    data = {'status': 0}
    if request.method == 'POST':
        receive_data = json.loads(request.body)
        if (receive_data and receive_data['username'] and receive_data['password']):
            userName = receive_data['username']
            password = receive_data['password']
            get_user = models.UserInfor.objects.get(userName=userName)  # 获取数据库数据
            if get_user:
                if (get_user.userName == userName and check_password(password,
                                                                     get_user.password)):  # 采用MD5进行密码加密。所以使用check_password方式进行密码检验
                    data['status'] = 1
                    request.session['userInfor'] = model_to_dict(get_user)
    return HttpResponse(json.dumps(data), content_type='application/json')  # 把数据以json格式返回给前台ajax


# ========================
# 2、用户注册
# ========================
def Register(request):
    data = {'status': 0}
    if request.method == 'POST':
        receive_data = json.loads(request.body)
        if receive_data['username'] and receive_data['password']:
            isExit = models.UserInfor.objects.filter(userName=receive_data['username'])
            if isExit:
                pass
            else:
                new_user = models.UserInfor(
                    userId=uuid.uuid1(),
                    userName=receive_data['username'],
                    password=make_password(receive_data['password']),
                    position='普通员工',
                    email=receive_data['email'],
                    name=receive_data['name'],
                    sex=receive_data['sex'],
                    tellPhone=receive_data['tellPhone'],
                    department=receive_data['department']
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


# ========================
# 4、获取用户信息
# ========================
def GetUserInfor(request):
    data = {'status': 0}
    if request.method == 'GET':
        userId = request.session.get('userInfor')['userId']
        try:
            userInfor = models.UserInfor.objects.get(userId=userId)
            data['status'] = 1
            data['userInfor'] = model_to_dict(userInfor)
        except:
            pass

    return HttpResponse(json.dumps(data), content_type='application/json')


# ========================
# 5、员工打卡
# ========================
def PunchIn(request):
    data = {'status': '0'}
    if request.method == 'POST':
        date = datetime.datetime.now()
        nowTime = date.strftime('%Y-%m-%d %H:%M:%S')
        begin = nowTime[0:10]
        end = (date + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')[0:10]

        userId = request.session.get('userInfor')['userId']

        isLeave = models.LeaveInfor.objects.raw(
            "SELECT * FROM app_leaveinfor WHERE userId='{0}' AND isApply=1 AND startTime BETWEEN '{1}' AND '{2}'".format(
                userId,
                begin, end))
        if len(isLeave) == 0:
            sql = 'SELECT * FROM app_attendenceinfor WHERE userId="{0}" AND startTime BETWEEN "{1}" AND "{2}"'.format(
                userId, begin, end)

            cursor = connection.cursor()
            cursor.execute(sql)
            temp = cursor.fetchone()
            cursor.close()

            try:
                if temp:
                    if temp[4]:
                        print('====')
                        data['status'] = '已打卡，无需重复打卡'
                    else:
                        models.AttendenceInfor.objects.update(endTime=nowTime)
                        data['status'] = '1'
                else:
                    userInfor = request.session.get('userInfor')
                    new_data = models.AttendenceInfor(
                        userId=userInfor['userId'],
                        name=userInfor['name'],
                        startTime=nowTime
                    )
                    new_data.save()
                    data['status'] = '1'
            except:
                pass

        else:
            data['status'] = '休假状态，无需打卡'

    print(data)
    return HttpResponse(json.dumps(data), content_type='application/json')


# ========================
# 6、修改员工信息
# ========================
def ChangeUserInfor(request):
    data = {'status': '服务器错误'}
    if request.method == 'POST':
        receive_data = json.loads(request.body)
        userId = request.session.get('userInfor')['userId']
        try:
            models.UserInfor.objects.filter(userId=userId).update(
                name=receive_data['name'],
                sex=receive_data['sex'],
                tellPhone=receive_data['tellPhone'],
                department=receive_data['department'],
                position=receive_data['position'],
                email=receive_data['email']
            )
            data['status'] = '1'
        except:
            data['status'] = '0'
    return HttpResponse(json.dumps(data), content_type='application/json')


# ========================
# 7、申请休假
# ========================
def ApplyLeave(request):
    data = {'status': '服务器错误'}
    if request.method == 'POST':
        receive_data = json.loads(request.body)
        if (receive_data and receive_data['startDate'] and receive_data['endDate']):
            print(receive_data)
            userInfor = request.session.get('userInfor')
            new_data = models.LeaveInfor(
                userId=userInfor['userId'],
                name=userInfor['name'],
                type=receive_data['type'],
                startTime=receive_data['startDate'][0:10],
                endTime=receive_data['endDate'][0:10],
                remark=receive_data['reason']
            )
            try:
                new_data.save()
                data['status'] = 1
            except:
                data['status'] = 0
        else:
            data['status'] = '请填写完整数据'
    return HttpResponse(json.dumps(data), content_type='application/json')
