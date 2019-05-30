from User.models import User
from utils.json_response import json_response
from django.db.models import ObjectDoesNotExist
from django.contrib import auth




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
        return json_response({
            'info': user.json()
        }, 200, user.token())
    return json_response(None, 500, 'Username duplicated')


def login(username, password):
    """
    Login check
    str:param username:
    str:param password:
    User Model:return: User object for success or None
    """
    user = auth.authenticate(username=username, password=password)
    if user:
        return json_response({
            'info': user.json()
        }, 200, user.token())
    return json_response(None, 400, 'Username not exist')


def follow(follower, followee):
    followee = get_user_or_none(followee)
    if follower and followee:
        follower.follow(followee)
        return json_response(None, 200, '%s stared %s success' % (follower.nickname, followee.nickname))
    return json_response(None, 400, 'Username not exist')


