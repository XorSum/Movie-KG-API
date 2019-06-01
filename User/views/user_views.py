import logging

from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from User.models import User
from utils.JWT import encode, login_required
from utils.json_response import json_response


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


def user_login(requests):
    """
     Login check
     str:param username:
     str:param password:
     User Model:return: User object for success or None
     """
    username = requests.POST.get('username', None)
    password = requests.POST.get('password', None)
    if username == None or password == None:
        return json_response(None, 400)
    logging.info('user login: username=%s, password=%s' % (username, password))
    user = auth.authenticate(username=username, password=password)
    if user:
        return json_response({
            'info': user.json()
        }, 200, encode(user))
    return json_response(None, 400, 'Username not exist')


def user_join(requests):
    """
    User register
    :param username:
    :param nickname:
    :param password:
    :return: JSON for success or None
    """
    username = requests.POST.get('username', None)
    nickname = requests.POST.get('nickname', None)
    password = requests.POST.get('password', None)
    if username == None or nickname == None or password == None:
        return json_response(None, 400)
    logging.info('user join: username=%s, nickname=%s, password=%s' % (username, nickname, password))
    try:
        User.objects.get(username=username)
    except ObjectDoesNotExist:
        user = User.objects.create_user(username=username, nickname=nickname, password=password)
        user.save()
        return json_response({
            'info': user.json()
        }, 200, encode(user))
    return json_response(None, 500, 'Username duplicated')


@login_required
def follow(requests, followee_name):
    followee = get_object_or_404(User, username=followee_name)
    follower = requests.GET['user']
    follower.following.add(followee)
    for article in followee.article_set.all():
        follower.feeds.add(article)
    logging.info('%s followed %s success' % (follower.username, followee.username))
    return json_response(None, 200, '%s followed %s success' % (follower.username, followee.username))


@login_required
def unfollow(requests, followee_name):
    followee = get_object_or_404(User, username=followee_name)
    follower = requests.GET['user']
    follower.following.remove(followee)
    for article in followee.article_set.all():
        follower.feeds.remove(article)
    logging.info('%s unfollowed %s success' % (follower.username, followee.username))
    return json_response(None, 200, '%s unfollowed %s success' % (follower.username, followee.username))


def user_list_followees(requests, username):
    user = get_object_or_404(User, username=username)
    logging.info('username=%s' % (username))
    rep = [i.json() for i in user.following.all()]

    return json_response(rep, 200)


def user_list_followers(requests, username):
    """
    返回关注的人的列表
    :return:
    """
    user = get_object_or_404(User, username=username)
    logging.info('username=%s' % (username))
    rep = [i.json() for i in User.objects.filter(following=user).all()]
    return json_response(rep, 200)