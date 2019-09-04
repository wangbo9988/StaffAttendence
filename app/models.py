from django.db import models
import uuid


# Create your models here.

# 员工信息表
class UserInfor(models.Model):
    userId = models.UUIDField(default=uuid.uuid4, primary_key=True, auto_created=True, editable=False)  # 编号
    userName = models.CharField(max_length=255)  # 用户名
    password = models.CharField(max_length=255)  # 密码
    name = models.CharField(max_length=50)  # 姓名
    sex = models.CharField(max_length=5)  # 性别
    position = models.CharField(max_length=255)  # 职位
    tellPhone = models.CharField(max_length=11)  # 联系方式
    email = models.CharField(max_length=50)  # 邮箱


# 出差记录表
class BusinessTravel(models.Model):
    userId = models.CharField(max_length=100)  # 编号
    name = models.CharField(max_length=50)  # 姓名
    type = models.CharField(max_length=20)  # 出差类型
    startTime = models.CharField(max_length=50)  # 起始时间
    endTime = models.CharField(max_length=50)  # 结束时间


# 加班申请表
class ApplyOverTime(models.Model):
    userId = models.CharField(max_length=100)  # 编号
    name = models.CharField(max_length=50)  # 姓名
    type = models.CharField(max_length=20)  # 加班类型
    startTime = models.CharField(max_length=50)  # 起始时间
    endTime = models.CharField(max_length=50)  # 结束时间
    isApply = models.BooleanField(default=False)  # 是否同意


# 请假记录表
class LeaveInfor(models.Model):
    userId = models.CharField(max_length=100)  # 编号
    name = models.CharField(max_length=50)  # 姓名
    type = models.CharField(max_length=20)  # 请假类型
    startTime = models.CharField(max_length=50)  # 起始时间
    endTime = models.CharField(max_length=50)  # 结束时间
    isApply = models.BooleanField(default=False)  # 是否同意

# 出勤记录表
class AttendenceInfor(models.Model):
    userId = models.CharField(max_length=100)  # 编号
    name = models.CharField(max_length=50)  # 姓名
    startTime = models.CharField(max_length=50)  # 起始时间
    endTime = models.CharField(max_length=50)  # 结束时间
