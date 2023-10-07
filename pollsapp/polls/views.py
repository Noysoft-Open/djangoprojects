from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("<h1>Hello World!</h1>")

def detail(request, question_id):
	return HttpResponse("<p>You are looking at question %s.</p>" % question_id)

def result(request, question_id):
	response = "<p>You're looking at the results of question %s.</p>"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("<p>You are voting on question %s.</p>" % question_id)