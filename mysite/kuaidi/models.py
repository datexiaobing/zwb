from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32, verbose_name="用户名")
    password = models.CharField(max_length=32, verbose_name="密码")
    nickname = models.CharField(max_length=32, verbose_name="姓名")
    phone = models.CharField(max_length=11, verbose_name="电话")
    email = models.EmailField(verbose_name="邮箱")
