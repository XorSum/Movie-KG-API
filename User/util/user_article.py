from utils.json_response import json_response
from User.util.user import username2user
from User.Article.models import Article
from User.util.article import get_article_or_none, article_list2json


@username2user
def view_article(user, post_id):
    """
    View article of user
    :param user:
    :param post_id:
    :return:
    """
    article = get_article_or_none(post_id)
    if article is None or article.user != user:
        return json_response(None, 400, 'Article not found')
    return json_response(article.json(), 200)


@username2user
def publish(user, content):
    """
    Publish an article
    :param user:
    :param content:
    :return: 201
    """
    try:
        Article.objects.create(user=user, content=content)
        user.article_count += 1
        user.save()
        return json_response(None, 201)
    except Exception:
        return json_response(None, 500)


@username2user
def article_list(user):
    """
    Get all articles of user
    :param user:
    :return: JSON response
    """
    ret = article_list2json(Article.objects.filter(user=user))
    return json_response({'articles': ret}, 200)


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
        user__in=user.stars.all()).order_by('-created_date')[lower - 1: upper]
    return json_response({'feeds': article_list2json(buf)}, 200)


