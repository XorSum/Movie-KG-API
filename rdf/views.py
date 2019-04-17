from django.shortcuts import render
from django.http import HttpResponse
from utils.query_main import AMI

ami = AMI()

def hello(request):
    return HttpResponse("hello world")

def query(request):
    question = request.GET.get('q')
    answer = ami.query(question)
    print(answer)
    return HttpResponse(str(answer))



