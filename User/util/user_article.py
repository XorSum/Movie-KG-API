from utils.json_response import json_response
from User.util.user import username2user
from User.util.article import  article_list2array
from User.Article.models import Article


@username2user
def view_article(user, post_id):
    ret = user.view(post_id)
    return json_response(ret, 200) if ret else json_response(None, 400, 'Article not found')


@username2user
def publish(user, content):
    user.publish(content)
    return json_response(None, 201)


@username2user
def article_list(user):
    return json_response({'articles': user.article_list()}, 200)


@username2user
def feed_pull(user, lower, upper):
    """
    Pull feeds in [lower, upper] of user
    :param user:
    :param lower:
    :param upper:
    :return: JSON response
    """
    buf = Article.objects.filter(
        user__in=user.following.all()).order_by('-created_date')[lower - 1: upper]
    return json_response({'feeds': article_list2array(buf)}, 200)


@username2user
def feed_push(user):
    pass


def get_feed(user):
    pass
