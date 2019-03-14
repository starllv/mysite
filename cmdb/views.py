from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from .models import Question
# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list':latest_question_list,
	}
	return render(request,'cmdb/index.html',context)
	
def detail(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request,'cmdb/detail.html',{'question':question})
	
def results(request,question_id):
	response = "你在看问题%s的结果"
	return HttpResponse(response%question_id)
	
def vote(request,question_id):
	return HttpResponse("你在给问题%s投票."%question_id)
