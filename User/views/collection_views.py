from django.shortcuts import get_object_or_404

from User.models import Article, Collection, User
from utils.JWT import login_required
from utils.json_response import json_response
from utils.page_range import get_range


@login_required
def article_in_which_collections(requests, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = requests.GET['user']
    result = []
    for each in user.favorites_set.all():
        data = {'collection_name': each.name,
                'collection_id': each.id,
                'private': each.private,
                'exits': each.articles.filter(id=article_id).count() > 0
                }
        result.append(data)
    return json_response(result, 200)


@login_required
def collection_add_article(requests, article_id, collection_id):
    user = requests.GET['user']
    collection = get_object_or_404(Collection, id=collection_id)
    article = get_object_or_404(Article, id=article_id)
    if collection.user != user:
        return json_response(None, 400)
    collection.articles.add(article)
    return json_response(collection.json(show_articles=True), 200)


@login_required
def collection_delete_article(requests, article_id, collection_id):
    user = requests.GET['user']
    collection = get_object_or_404(Collection, id=collection_id)
    article = get_object_or_404(Article, id=article_id)
    if collection.user != user:
        return json_response(None, 400)
    collection.articles.remove(article)
    return json_response(collection.json(show_articles=True), 200)


@login_required
def collection_list_article(requests, collection_id):
    try:
        start,end = get_range(requests)
        collection = Collection.objects.get(id=collection_id)
        if collection.private == True and requests.GET['user'] != collection.user:
            return json_response(None, 400)
        total = collection.articles.count()
        articles = collection.articles.all()[start:end]
        rep = [each.json() for each in articles]
        return json_response(rep, 200,start=start,end=end,total=total)
    except:
        return json_response(None, 400)


@login_required
def user_create_collection(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name', None)
        private = requests.POST.get('private', None)
        if name == None or private == None:
            return json_response(None, 400)
        collection = Collection.objects.create(user=requests.GET['user'], name=name, private=private)
        return json_response(collection.json(), 200)
    else:
        return json_response(None, 400, 'post')


@login_required
def user_list_all_collection(requests):
    user = requests.GET['user']
    collections = user.collection_set.all()
    rep = [each.json() for each in collections]
    return json_response(rep, 200)


def user_list_public_collection(requests):
    username = requests.GET.get('username', None)
    user = User.objects.get(username=username)
    if user == None:
        return json_response(None, 400)
    collections = user.collection_set.filter(private=False).all()
    rep = [each.json() for each in collections]
    return json_response(rep, 200)