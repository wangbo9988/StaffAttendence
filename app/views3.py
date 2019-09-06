from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.db import connection

from app import models

import datetime
import json
import uuid


# Create your views here.

#   功能模块：管理员操作模块
# 1、GetLeaveRecord 获取请假记录
# 2、SubmitRecord 提交请假审核结果
#


# ========================
# 1、获取请假记录
# ========================
def GetLeaveRecord(request):
    data = []
    if request.method == 'GET':
        leaveRecordList = models.LeaveInfor.objects.all()
        leaveRecord = []

        for temp in leaveRecordList:
            record = {}
            record['userId'] = model_to_dict(temp)['userId']
            record['name'] = model_to_dict(temp)['name']
            record['type'] = model_to_dict(temp)['type']
            record['startTime'] = model_to_dict(temp)['startTime']
            record['endTime'] = model_to_dict(temp)['endTime']
            record['isApply'] = model_to_dict(temp)['isApply']
            record['id'] = model_to_dict(temp)['id']
            data.append(record)
    return HttpResponse(json.dumps(data), content_type='application/json')


# ========================
# 2、提交请假审核结果
# ========================
def SubmitRecord(request):
    data = {'status': '3'}
    if request.method == "POST":
        receive_data = json.loads(request.body)
        try:
            models.LeaveInfor.objects.filter(id=receive_data['id']).update(
                startTime=receive_data['leava_start'], endTime=receive_data['leava_stop'],
                isApply=receive_data['status'])
            data['status'] = '1'
        except:
            data['status'] = '0'
    print(data)
    return HttpResponse(json.dumps(data), content_type='application/json')


# ========================
# 3、获取员工信息
# ========================
def GetEmployInfor(request):
    data = []
    if request.method == 'GET':
        try:
            lists = models.UserInfor.objects.all()
            for temp in lists:
                temp = model_to_dict(temp)
                userList = {}
                if (temp['name'] and temp['position'] != '管理员'):
                    userList['userId'] = temp['userId']
                    userList['name'] = temp['name']
                    userList['tellPhone'] = temp['tellPhone']
                    userList['department'] = temp['department']
                    userList['position'] = temp['position']
                    userList['email'] = temp['email']
                    userList['sex'] = temp['sex']
                    data.append(userList)
        except:
            pass
    return HttpResponse(json.dumps(data), content_type='application/json')


# ========================
# 4、提交员工信息
# ========================
def SubmitEmployInfor(request):
    data = {'status': '2'}
    if request.method == 'POST':
        receive_data = json.loads(request.body)
        try:
            models.UserInfor.objects.filter(userId=receive_data['id']).update(department=receive_data['department'],
                                                                              position=receive_data['position'])
            data['status'] = '1'
        except:
            data['status'] = '0'
    return HttpResponse(json.dumps(data), content_type='application/json')
