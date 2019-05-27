from User.models import User
from utils.json_response import json_response
from django.db.models import ObjectDoesNotExist
from django.contrib import auth


def username2user(func):
    def wrapper(user, *args, **kwargs):
        try:
            user = User.objects.get(username=user)
        except ObjectDoesNotExist:
            return json_response(None, 400, 'Username not exist')
        return func(user, *args, **kwargs)
    return wrapper


def get_user_or_none(user):
    """
    Query username from db
    :param user:
    :return: object or None
    """
    try:
        user = User.objects.get(username=user)
    except ObjectDoesNotExist:
        return None
    return user


def join(username, nickname, password):
    """
    User register
    :param username:
    :param nickname:
    :param password:
    :return: JSON for success or None
    """
    try:
        User.objects.get(username=username)
    except ObjectDoesNotExist:
        user = User.objects.create_user(username=username, nickname=nickname, password=password)
        user.save()
        return json_response(None, 201)
    return json_response(None, 500, 'Username duplicated')


def login(username, password):
    """
    Login check
    :param username:
    :param password:
    :return: User object for success or None
    """
    user = auth.authenticate(username=username, password=password)
    if user:
        return json_response({
            'token': 'Hello World!',
            'info': user.json()
        }, 200)
    return json_response(None, 400, 'Username not exist')
    

def follow(follower, followee):
    follower = get_user_or_none(follower)
    followee = get_user_or_none(followee)
    if follower and followee:
        follower.follow(followee)
        return json_response(None, 200, '%s stared %s success' % (follower.nickname, followee.nickname))
    return json_response(None, 400, 'Username not exist')


@username2user
def follow_list(user):
    return json_response({'list': user.follow_list()}, 200)
