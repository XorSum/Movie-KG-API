from django.shortcuts import HttpResponse, Http404
from users import models as data
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth


@csrf_exempt
def login(requests):
    username = requests.POST['username']
    password = requests.POST['password']
    if '@' not in username:
        try:
            user = data.User.objects.get(username=username)
        except data.models.ObjectDoesNotExist:
            return HttpResponse('fail')
        else:
            username = user.email
    user = auth.authenticate(requests, email=username, password=password)
    if user is not None:
        return HttpResponse(user.username)
    return HttpResponse('fail')


@csrf_exempt
def join(requests):
    email = requests.POST['email']
    nickname = requests.POST['nickname']
    password = requests.POST['password']
    try:
        data.User.objects.get(email=email)
    except data.models.ObjectDoesNotExist:
        user = data.User.objects.create_user(email=email, nickname=nickname, password=password)
        user.save()
        return HttpResponse(user.username)
    return HttpResponse('email duplicated')
