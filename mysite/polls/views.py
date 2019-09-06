# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Address
from django.template import loader

# Create your views here.

def ins(request):

	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template=loader.get_template('polls/index.html')
	context={
			"latest_question_list" : latest_question_list,
			}

	if request.method == "POST" and request.POST:
		# dic={}
		# for key in request.POST:
		# 	print(key)
		# 	valuelist = request.POST.getlist(key)
		# 	print(valuelist) 
		# 	dic[key]=valuelist

		name = request.POST.get("name_2")
		tel = request.POST.get("tel_2",None)
		full = request.POST.get("addr_full",None)
		# try:
		pro=full.split('--')[0]
		# pro=request.POST.get("prov_02")
		city=full.split('--')[1]
		town=full.split('--')[2]
		# except IndexError:
		# 	pro=0
		# 	city=0
		# 	town=0
		addr=request.POST.get('addr_2')
		kd=request.POST.get('di_02')
		Address.objects.create(
			name=name,
			telphone=tel,
			province=pro,
			city=city,
			town=town,
			addr=addr,
			kd=kd,
			)
			
	info_list=Address.objects.all()
	# info_list=dic
	
	return HttpResponse(template.render({"info_list":info_list},request))

def detail(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template=loader.get_template('polls/Addr.html')
	context={
			"latest_question_list" : latest_question_list,
			}
	return HttpResponse(template.render(context,request))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)	