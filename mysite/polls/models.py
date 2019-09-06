from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('发布时间')
    def __str__(self):
    	return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
    	return self.choice_text

class Address(models.Model):
	name=models.CharField(max_length=200)
	telphone=models.IntegerField()
	province=models.CharField(max_length=200)
	city=models.CharField(max_length=200)
	town=models.CharField(max_length=200)
	addr=models.CharField(max_length=200)
	date=models.DateField(auto_now_add=True)
	datetime=models.DateTimeField(auto_now_add=True)
	kd=models.CharField(max_length=200)#快递类型
	obj_type=models.CharField(max_length=200)#寄什么物品
	send_name=models.CharField(max_length=200)
	send_tel=models.IntegerField(default=0)
	send_bumen=models.CharField(max_length=200)
	send_addr=models.CharField(max_length=200)
