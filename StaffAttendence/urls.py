"""StaffAttendence URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views, views2, views3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views2.ToLogin),  # 跳转到登录界面
    path('toRegister/', views2.ToRegister),  # 跳转到注册界面
    path('toIndex/', views2.ToIndex),  # 跳转到主界面
    path('toApplyLeave/', views2.ToApplyLeave),  # 跳转到申请休假界面
    path('toPersonalInfor/', views2.ToPersonalInfor),  # 跳转到申请休假界面
    path('toAttence/', views2.ToAttence),  # 跳转到勤管理界面
    path('toDepartment/', views2.ToDepartment),  # 跳转到部门管理界面
    path('toLeaveRecord/', views2.ToLeaveRecord),  # 跳转到请假记录界面
    path('toAttencrResult/', views2.ToAttencrResult),  # 跳转到考勤记录界面
    path('toResult/', views2.ToResult),  # 跳转到考勤结果界面
    path('toEmployeeManage/', views2.ToEmployeeManage),  # 跳转到员工信息界面
    path('toDepartment/', views2.ToDepartment),  # 跳转到部门管理界面
    path('toLeaveRecord/', views2.ToLeaveRecord),  # 跳转到请假管理界面
    path('login/', views.Login),  # 用户登录
    path('LoginOut/', views.LoginOut),  # 用户登出
    path('Register/', views.Register),  # 用户注册
    path('getUserInfor/', views.GetUserInfor),  # 获取用户信息
    path('punchIns/', views.PunchIn),  # 员工打卡
    path('changeUserInfor/', views.ChangeUserInfor),  # 修改用户信息
    path('applyLeave/', views.ApplyLeave),  # 申请休假
    path('getLeaveRecord/', views3.GetLeaveRecord),  # 请假记录
    path('submitRecord/', views3.SubmitRecord),  # 提交请假审核结果
    path('getEmployInfor/', views3.GetEmployInfor),  # 提交请假审核结果
    path('submitEmployInfor/', views3.SubmitEmployInfor),  # 提交请假审核结果
    path('getResult/', views3.GetResult),  # 获取考核结果
    path('getAttenceResult/', views3.GetAttenceResult),  # 获取考核记录
    path('getLeaveResult/', views3.GetLeaveResult),  # 获取请假记录
]
