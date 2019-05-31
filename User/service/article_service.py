import logging

from User.models import User
from utils.json_response import json_response
from User.models.article import Article
from django.db.models import ObjectDoesNotExist



def publish(user, content,movie,person):
    """
        Publish an article
        :param content:
        :return: None
     """
    article = Article.objects.create(content=content, user=user)
    followers = User.objects.filter(following=user).all()  # 我关注的人
    for each in followers:
        each.feeds.add(article)
    return json_response(article.json(), 200)


def get_feeds_fast(user, lower, upper):
    """
    Same as feeds_pull, but using offline user.feeds
    :param user:
    :param lower:
    :param upper:
    :return: JSON response
    """
    lower = max(lower, 0)
    upper = min(upper, lower + 20)
    buf = user.feeds.all().order_by('-created_date')[lower:upper]
    logging.info('feddpull user=%s, lower=%s, upper=%s' % (user.username, lower, upper))
    return json_response({'feeds': [each.json() for each in buf],
                          'lower': lower,
                          'upper': upper,
                          'total': user.feeds.count()}, 200)
