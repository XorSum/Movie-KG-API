import logging

from django.shortcuts import get_object_or_404

from Subject.models import Movie, Person
from User.models import Article, User, History
from utils.JWT import login_required
from utils.json_response import json_response
from utils.page_range import get_range


@login_required
def user_publish_article(requests):
    content = requests.POST.get('content', None)
    movie_id = requests.POST.get('movie_id', None)
    if movie_id != None:
        movie = get_object_or_404(Movie, id=movie_id)
    else:
        movie = None
    person_id = requests.POST.get('person_id', None)
    if person_id != None:
        person = get_object_or_404(Person, id=person_id)
    else:
        person = None
    logging.info('contents= %s' % (content))
    user = requests.GET['user']
    article = Article.objects.create(content=content, user=user, movie=movie, person=person)
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
        start, end = get_range(requests)
    except:
        return json_response('', 400)
    total = user.article_set.count()
    articles = user.article_set.all().order_by('-created_date')[start:end]
    rep = [each.json() for each in articles]
    return json_response(rep, 200, start=start, end=end, total=total)


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
        start, end = get_range(requests)
        logging.info("start=%s, end=%s" % (start, end))
        total = user.history_set.count()
        histories = user.history_set.all().order_by('-created_date')[start:end]
        rep = [i.json() for i in histories]
        return json_response(rep, 200, start=start, end=end, total=total)
    except:
        return json_response(False, 400)


@login_required
def user_pull_feeds(requests):
    """
       Same as feeds_pull, but using offline user.feeds
       :param start:
       :param end:
       :return: JSON response
    """
    try:
        start, end = get_range(requests)
        user = requests.GET['user']
        total = user.feeds.count()
        buf = user.feeds.all().order_by('-created_date')[start:end]
        logging.info('feddpull user=%s, start=%s, end=%s' % (user.username, start, end))
        return json_response([each.json() for each in buf], 200, start=start, end=end, total=total)
    except:
        return json_response(None, 400)
