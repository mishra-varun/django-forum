from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question


def index(request):
	latest_question_list = Question.objects.all() #.order_by('-pub_date')
	op = ', '.join(q.qtext for q in latest_question_list)
	#template=loader.get_template('polls/index.html')
	context={'latest_question_list':latest_question_list,}
	#return HttpResponse(template.render(context,request))
	return render(request, 'polls/index.html', context)


def detail(request, qid):
	return HttpResponse("Question no. %s" % qid)


def results(request, qid):
	return HttpResponse("The result for question no. %s" % qid)


def vote(request, qid):
	return HttpResponse("Vote on question no. %s" % qid)