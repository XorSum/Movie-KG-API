import requests
import os

user = []
n = 5


def get(path, params=None):
    return requests.api.get('http://localhost:8000/api/v1' + path, params)


def post(path, data=None, json=None):
    return requests.api.post('http://localhost:8000/api/v1' + path, data, json)


def register(username, nickname, password='password'):
    post('/user/join', data={
        'username': username,
        'nickname': nickname,
        'password': password
    })


def star(follower, followee):
    get('/user/%s/star/%s' % (follower, followee))


def publish(username, content):
    post('/user/%s/publish' % username, data={
        'content': content,
    })


def articles(username):
    return get('/user/%s/articles' % username).json()['data']['articles']


def feeds(username, lower, upper):
    return get('/user/%s/feeds?range=%d,%d' % (username, lower, upper)).json()['data']['feeds']
