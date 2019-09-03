from django.db import models
import uuid


# Create your models here.
class UserInfor(models.Model):
    userId = models.UUIDField(default=uuid.uuid4, primary_key=True, auto_created=True, editable=False)  # 身份标示码
    userName = models.CharField(max_length=255)  # 用户名
    password = models.CharField(max_length=255)  # 密码
    name = models.CharField(max_length=50)  # 姓名
    workId = models.IntegerField()  # 工号
    department = models.CharField(max_length=255)  # 部门
    position = models.CharField(max_length=255)  # 职位
    tellPhone = models.CharField(max_length=11)  # 手机号
