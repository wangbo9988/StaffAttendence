from django.db import models
import uuid


# Create your models here.

# 员工信息表
class UserInfor(models.Model):
    userId = models.CharField(primary_key=True, max_length=255)  # 编号
    userName = models.CharField(max_length=255)  # 用户名
    password = models.CharField(max_length=255)  # 密码
    sex = models.CharField(max_length=5)  # 性别
    name = models.CharField(max_length=255, null=True)  # 姓名
    position = models.CharField(max_length=255, null=True)  # 职位
    department = models.CharField(max_length=255, null=True)  # 部门
    tellPhone = models.CharField(max_length=11, null=True)  # 联系方式
    email = models.CharField(max_length=50, null=True)  # 邮箱


# 加班申请表
class ApplyOverTime(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)  # 记录编号
    userId = models.CharField(max_length=100)  # 编号
    name = models.CharField(max_length=50)  # 姓名
    type = models.CharField(max_length=20)  # 加班类型
    startTime = models.CharField(max_length=50, default=None)  # 起始时间
    endTime = models.CharField(max_length=50, default=None)  # 结束时间
    isApply = models.BooleanField(default=False)  # 是否同意


# 请假记录表
class LeaveInfor(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)  # 记录编号
    userId = models.CharField(max_length=100)  # 编号
    name = models.CharField(max_length=50)  # 姓名
    type = models.CharField(max_length=20)  # 请假类型
    startTime = models.CharField(max_length=50, default=None)  # 起始时间
    endTime = models.CharField(max_length=50, default=None)  # 结束时间
    remark = models.CharField(max_length=255, null=True)  # 备注
    isApply = models.CharField(default='待审核', max_length=50)  # 是否同意


# 出勤记录表
class AttendenceInfor(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)  # 记录编号
    userId = models.CharField(max_length=100)  # 编号
    name = models.CharField(max_length=50)  # 姓名
    startTime = models.CharField(max_length=50, default=None)  # 起始时间
    endTime = models.CharField(max_length=50, default=None)  # 结束时间


