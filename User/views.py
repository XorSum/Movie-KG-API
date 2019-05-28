from utils.json_response import json_response
from User.util import user as user_util, user_article, article as article_util


def login(requests):
    username = requests.POST['username']
    password = requests.POST['password']
    return user_util.login(username=username, password=password)


def join(requests):
    username = requests.POST['username']
    nickname = requests.POST['nickname']
    password = requests.POST['password']
    return user_util.join(username=username, nickname=nickname, password=password)


def user_detail(requests, username):
    user = user_util.get_user_or_none(username)
    return json_response(user.json(), 200) if user else json_response(None, 400, 'Username not exist')


def follow(requests, username, __username):
    return user_util.follow(username, __username)


def follow_list(requests, username):
    return user_util.follow_list(user=username)


def publish(requests, username):
    content = requests.POST['content']
    return user_article.publish(username, content)


def article_list(requests, username):
    return user_article.article_list(username)


def view_article(requests, username, post_id):
    return user_article.view_article(username, post_id)


def feed_pull(requests, username):
    """
    return feed [lower, upper] of username
    """
    lower, upper = map(int, requests.GET['range'].split(','))
    return user_article.get_feeds(username, lower, upper)

