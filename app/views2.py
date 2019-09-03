from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.sessions.models import Session
from app import models

import json


# Create your views here.

#   功能模块：页面跳转模块
# 1、ToLogin 跳转到登录页
# 2、ToRegister 跳转到注册页
# 3、ToIndex 跳转到主界面
# 4、ToApplyLeave 跳转到申请休假界面
# 5、ToPersonalInfor 跳转到个人信息界面
# 6、ToAttence 跳转到勤管理界面
# 7、ToDepartment 跳转到部门管理界面
# 8、ToLeaveRecord 跳转到请假记录界面
# 9、ToResult 跳转到考勤结果界面
#


# ========================
# 1、跳转到登录页
# ========================
def ToLogin(request):
    return render(request, 'login.html', {})


# ========================
# 2、跳转到注册页
# ========================
def ToRegister(request):
    return render(request, 'register.html', {})


# ========================
# 3、跳转到主界面
# ========================
def ToIndex(request):
    userInfor = request.session.get('userInfor')
    if userInfor['position'] == '0':
        return render(request, 'admin/attence.html', {})
    else:
        return render(request, 'staff/punch.html', {})


# ========================
# 4、跳转到申请休假界面
# ========================
def ToApplyLeave(request):
    return render(request, 'staff/applyLeave.html', {})


# ========================
# 5、跳转到个人信息界面
# ========================
def ToPersonalInfor(request):
    return render(request, 'staff/personalInfor.html', {})


# ========================
# 6、跳转到勤管理界面
# ========================
def ToAttence(request):
    return render(request, 'admin/attence.html', {})


# ========================
# 7、跳转到部门管理界面
# ========================
def ToDepartment(request):
    return render(request, 'admin/department.html', {})


# ========================
# 8、跳转到请假记录界面
# ========================
def ToLeaveRecord(request):
    return render(request, 'admin/leaveRecord.html', {})


# ========================
# 9、跳转到考勤结果界面
# ========================
def ToResult(request):
    return render(request, 'admin/result.htmll', {})
