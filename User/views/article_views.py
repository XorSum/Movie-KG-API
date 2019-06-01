import logging

from django.shortcuts import get_object_or_404

from User.models import Article, User, History
from utils.JWT import login_required
from utils.json_response import json_response


@login_required
def user_publish_article(requests):
    content = requests.POST.get('content', None)
    logging.info('contents= %s' % (content))
    user = requests.GET['user']
    article = Article.objects.create(content=content, user=user)
    followers = User.objects.filter(following=user).all()  # 我关注的人
    for each in followers:
        each.feeds.add(article)
    return json_response(article.json(), 200)


def user_list_article(requests, username):
    """
      :param username:
      :param lower:
      :param upper:
      :return: JSON response
   """
    try:
        logging.info('username=%s' % (username))
        user = get_object_or_404(User, username=username)
        lower = int(requests.GET['lower'])
        upper = int(requests.GET['upper'])
    except:
        return json_response('', 400)
    lower = max(lower, 0)
    upper = min(upper, lower + 20)
    articles = user.article_set.all().order_by('-created_date')[lower:upper]
    rep = [each.json() for each in articles]
    return json_response(rep, 200)


@login_required
def user_read_article(requests, article_id):
    """
    增加一条阅读记录
    :param article_id:
    :param token
    :return: None
    """
    try:
        user = requests.GET['user']
        article = get_object_or_404(Article, id=article_id)
        History.objects.create(user=user, article=article)
        return json_response(True, 200)
    except:
        return json_response(False, 400)


@login_required
def user_history_article(requests):
    """
    获取阅读历史
    :return: list of ReadHistories
    """
    try:
        user = requests.GET['user']
        histories = user.readhistory_set.all().order_by('-created_date')
        rep = [i.json() for i in histories]
        return json_response(rep, 200)
    except:
        return json_response(False, 400)


@login_required
def user_pull_feeds(requests):
    """
           Same as feeds_pull, but using offline user.feeds
           :param lower:
           :param upper:
           :return: JSON response
    """
    try:
        lower = int(requests.GET['lower'])
        upper = int(requests.GET['upper'])
    except:
        return json_response(None, 400)

    lower = max(lower, 0)
    upper = min(upper, lower + 20)
    user = requests.GET['user']
    buf = user.feeds.all().order_by('-created_date')[lower:upper]
    logging.info('feddpull user=%s, lower=%s, upper=%s' % (user.username, lower, upper))
    return json_response({'feeds': [each.json() for each in buf],
                          'lower': lower,
                          'upper': upper,
                          'total': user.feeds.count()}, 200)