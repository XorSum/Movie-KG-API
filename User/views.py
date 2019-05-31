import logging

from django.shortcuts import get_object_or_404

from User.models import User, Article, Favorites
from utils.json_response import json_response
from utils.JWT import login_required
from User.service import user_service as user_util, article_service


def none2reponse(func):
    """
    如过func的返回值是None,则将返回值修改为json_response(None,500)
    :param func:
    :return: json_response
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == None:
            result = json_response(None, 500)
        return result

    return wrapper


def login(requests):
    username = requests.POST.get('username', None)
    password = requests.POST.get('password', None)
    if username == None or password == None:
        return json_response(None, 400)
    logging.info('user login: username=%s, password=%s' % (username, password))
    return user_util.login(username=username, password=password)


def join(requests):
    username = requests.POST.get('username', None)
    nickname = requests.POST.get('nickname', None)
    password = requests.POST.get('password', None)
    if username == None or nickname == None or password == None:
        return json_response(None, 400)
    logging.info('user join: username=%s, nickname=%s, password=%s' % (username, nickname, password))
    return user_util.join(username=username, nickname=nickname, password=password)


@login_required
def publish(requests):
    content = requests.POST.get('content', None)
    logging.info('contents= %s' % (content))
    return article_service.publish(user=requests.GET['user'], content=content,
                                   movie=None, person=None)


@login_required
def in_which_favorites(requests, post_id):
    article = get_object_or_404(Article, post_id=post_id)
    user = requests.GET['user']
    result = []
    for each in user.favorites_set.all():
        data = {'favorites_name': each.name,
                'favorites_id': each.id,
                'private': each.private,
                'exits': each.articles.filter(post_id=post_id).count() > 0
                }
        result.append(data)
    return json_response({'favorites': result}, 200)


@login_required
def add_favorites(requests, post_id, favorites_id):
    user = requests.GET['user']
    favorite = get_object_or_404(Favorites, id=favorites_id)
    article = get_object_or_404(Article, post_id=post_id)
    if favorite.user != user:
        return json_response(None, 400)
    favorite.articles.add(article)
    return json_response(favorite.json(show_articles=True), 200)


@login_required
def delete_favorites(requests, post_id, favorites_id):
    user = requests.GET['user']
    favorite = get_object_or_404(Favorites, id=favorites_id)
    article = get_object_or_404(Article, post_id=post_id)
    if favorite.user != user:
        return json_response(None, 400)
    favorite.articles.remove(article)
    return json_response(favorite.json(show_articles=True), 200)


@login_required
def create_favorites(requests):
    name = requests.GET.get('name', None)
    private = requests.GET.get('private', None)
    if name == None or private == None:
        return json_response(None, 400)
    favorite = Favorites.objects.create(user=requests.GET['user'], name=name, private=private)
    return json_response(favorite.json(), 200)


@login_required
def follow(requests, followee_name):
    followee = get_object_or_404(User, username=followee_name)
    return user_util.follow(follower=requests.GET['user'], followee=followee)


@login_required
def feed_pull(requests):
    """
    return feed [lower, upper] of username
    """
    try:
        lower = int(requests.GET['lower'])
        upper = int(requests.GET['upper'])
    except:
        return json_response(None, 400)
    return article_service.get_feeds_fast(requests.GET['user'], lower, upper)


def get_article_list(requests, username):
    try:
        logging.info('username=%s' % (username))
        user = User.objects.get(username=username)
    except:
        return json_response('', 400)

    return json_response(user.article_list(), 200)


def get_public_favorites(requests, username):
    try:
        logging.info('username=%s' % (username))
        user = User.objects.get(username=username)
    except:
        return json_response('', 400)
    return json_response(user.get_favorites_list(), 200)


def get_favorites(requests, username, favorite_id):
    try:
        logging.info('username=%s' % (username))
        user = User.objects.get(username=username)
        favorite = user.favorites_set.get(id=favorite_id)
    except:
        return json_response('', 400)
    return json_response(favorite.json(show_articles=True), 200)


def get_followers(requests, username):
    try:
        logging.info('username=%s' % (username))
        user = User.objects.get(username=username)
    except:
        return json_response('', 400)
    return json_response(user.follow_list(), 200)


def get_idols(requests, username):
    try:
        logging.info('username=%s' % (username))
        user = User.objects.get(username=username)
    except:
        return json_response('', 400)
    return json_response(user.idol_list(), 200)
