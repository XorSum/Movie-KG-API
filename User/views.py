from utils.json_response import json_response
from utils.JWT import login_required
from User.util import user as user_util, user_article


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
    user = user_util.get_user_or_none(user=username)
    return json_response(user.json(), 200) if user else json_response(None, 400, 'Username not exist')


@login_required
def follow(requests, __username):
    return user_util.follow(follower=requests.GET['token'], followee=__username)


@login_required
def follow_list(requests):
    return user_util.follow_list(user=requests.GET['token'])


@login_required
def publish(requests):
    content = requests.POST['content']
    return user_article.publish(user=requests.GET['token'], content=content)


@login_required
def article_list(requests):
    return user_article.article_list(user=requests.GET['token'])


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
