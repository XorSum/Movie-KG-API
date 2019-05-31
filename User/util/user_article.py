import logging

from utils.json_response import json_response
from User.models.article import Article
from django.db.models import ObjectDoesNotExist


def view_article(user, post_id):
    try:
        article = Article.objects.get(post_id=post_id)
    except ObjectDoesNotExist:
        return json_response(None, 400, 'Article not found')
    return json_response(article.json(), 200) if article.user == user else json_response(None, 400, 'Article not found')


def publish(user, content):
    article = user.publish(content)
    return json_response(article.json(), 200)


def get_feeds_slow(user, lower, upper):
    """
    Pull feeds in [lower, upper] of user
    :param user:
    :param lower:
    :param upper:
    :return: JSON response
    """
    logging.info("get_feeds_slow user=%s, lower=%s, upper=%s"%(user.username,lower,upper))
    lower = max(0,lower)
    upper = min(upper,lower+20)
    buf = Article.objects.filter(
        user__in=user.following.all()).union(user.article_set.all()).order_by('-created_date')[lower : upper]
    return json_response({'feeds': [each.json() for each in buf]}, 200)


def get_feeds_fast(user, lower, upper):
    """
    Same as feeds_pull, but using offline user.feeds
    :param user:
    :param lower:
    :param upper:
    :return: JSON response
    """
    logging.info("get_feeds_fast user=%s, lower=%s, upper=%s" % (user.username, lower, upper))
    buf = user.get_feeds(lower, upper)
    return json_response({'feeds': [each.json() for each in buf]}, 200)
