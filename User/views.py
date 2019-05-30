from User.models import User
from utils.json_response import json_response
from utils.JWT import login_required, post
from User.util import user as user_util, user_article


@post
def login(requests):
    username = requests.POST['username']
    password = requests.POST['password']
    return user_util.login(username=username, password=password)


@post
def join(requests):
    username = requests.POST['username']
    nickname = requests.POST['nickname']
    password = requests.POST['password']
    return user_util.join(username=username, nickname=nickname, password=password)


def user_detail(requests, username):
    user = user_util.get_user_or_none(user=username)
    return json_response(user.json(), 200) if user else json_response(None, 400, 'Username not exist')


@login_required
def follow(requests, followee):
    return user_util.follow(follower=requests.GET['token'], followee=followee)


@login_required
def publish(requests):
    content = requests.POST['content']
    return user_article.publish(user=requests.GET['token'], content=content)


@login_required
def view_article(requests, username, post_id):
    return user_article.view_article(user=username, post_id=post_id)


@login_required
def feed_pull(requests):
    """
    return feed [lower, upper] of username
    """
    lower, upper = map(int, requests.GET['range'].split(','))
    return user_article.get_feeds(requests.GET['token'], lower, upper)


def get_article_list(requests, username):
    try:
        print("username=", username)
        user = User.objects.get(username=username)
    except:
        return json_response('', 400)

    return json_response(user.article_list(), 200)


def get_public_favorites(requests, username):
    try:
        print("username=", username)
        user = User.objects.get(username=username)
    except:
        return json_response('', 400)
    return json_response(user.get_favorites_list(), 200)


def get_favorites(requests, username, favorite_id):
    try:
        print("username=", username)
        user = User.objects.get(username=username)
        favorite = user.favorites_set.get(id=favorite_id)
    except:
        return json_response('', 400)
    return json_response(favorite.json(show_articles=True), 200)


def get_followers(requests, username):
    try:
        print("username=", username)
        user = User.objects.get(username=username)
    except:
        return json_response('', 400)
    return json_response(user.follow_list(), 200)


def get_idols(requests, username):
    try:
        print("username=", username)
        user = User.objects.get(username=username)
    except:
        return json_response('', 400)
    return json_response(user.idol_list(), 200)
