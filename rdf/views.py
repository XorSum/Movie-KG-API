from django.shortcuts import render
from django.http import HttpResponse
from utils.query_main import AMI
from urllib import parse

ami = AMI()

def hello(request):
    return HttpResponse("hello world")

def search(request):
    question = request.GET.get('question')
    question = parse.unquote(question)
    answer = ami.query(question)
    print(answer)
    return HttpResponse(str(answer))


def relationTo(request):
    question = request.GET.get('subject')
    question = parse.unquote(question)
    answer = ami.relationTo(question)
    print(answer)
    return HttpResponse(str(answer))

def relationFrom(request):
    question = request.GET.get('object')
    question = parse.unquote(question)
    answer = ami.relationFrom(question)
    print(answer)
    return HttpResponse(str(answer))

def getUrl(request):
    question = request.GET.get('name')
    question = parse.unquote(question)
    answer = ami.getUrl(question)
    print(answer)
    return HttpResponse(str(answer))



def help(request):
    s = """    
1. 某演员演了什么电影
2. 某电影有哪些演员出演
3. 演员A和演员B合作出演了哪些电影
4. 某演员参演的评分大于X的电影有哪些
5. 某演员出演过哪些类型的电影
6. 某演员出演的XX类型电影有哪些。
7. 某演员出演了多少部电影。
8. 某演员是喜剧演员吗。
9. 某演员的生日/出生地/英文名/简介
10. 某电影的简介/上映日期/评分
"""
    return HttpResponse(s)