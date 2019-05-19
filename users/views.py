from django.shortcuts import HttpResponse, Http404
from users import models as data
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from utils.json_response import json_response
from utils.user import get_user_or_none


@csrf_exempt
def login(requests):
    username = requests.POST['username']
    password = requests.POST['password']
    user = auth.authenticate(requests, username=username, password=password)
    if user is not None:
        return json_response({
            'token': 'Hello World!',
            'username': user.username,
            'nickname': user.nickname,
        }, 200)
    return json_response(None, 400, 'Username not exist')


@csrf_exempt
def join(requests):
    username = requests.POST['username']
    nickname = requests.POST['nickname']
    password = requests.POST['password']
    try:
        data.User.objects.get(username=username)
    except data.models.ObjectDoesNotExist:
        user = data.User.objects.create_user(username=username, nickname=nickname, password=password)
        user.save()
        return json_response(None, 201)
    return json_response(None, 500, 'Username duplicated')


def log(requests, username):
    user = get_user_or_none(username)
    return json_response(None, 400, 'Username not exist') if user is None else json_response({
        'username': user.username,
        'nickname': user.nickname,
    }, 200)


def star(requests, username, __username):
    follower = get_user_or_none(username)
    followed = get_user_or_none(__username)
    if follower is None or followed is None:
        return json_response(None, 400, 'Username not exist')

    follower.stars.add(followed)
    return json_response(None, 200, '%s stared %s success' % (follower.nickname, followed.nickname))


def star_list(requests, username):
    user = get_user_or_none(username)
    if user is None:
        return json_response(None, 400, 'Username not exist')
    lst = []
    for each in user.stars.all():
        lst.append('%s(%s)' % (each.nickname, each.username))
    return json_response({
        'list': lst
    }, 200)
