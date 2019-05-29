from django.test import TestCase

from User.models.favorites import Favorites
from User.util import user, user_article
from User.models import User, Article
import json


def s(name, i):
    return '%s%s' % (name, i)


def json_response2json(response):
    return json.loads(response.content.decode())


class UserTestCase(TestCase):
    n = 5

    @classmethod
    def setUpTestData(cls):
        """
        Create 5 user named user_i (i from 0 to 4), then user0 star all user
        :return:
        """
        for i in range(cls.n):
            user.join(username=s('user', i), nickname=s('nick', i), password='test')
        for i in range(1, cls.n):
            user.follow('user0', s('user', i))
        for i in range(cls.n << 2):
            user_article.publish(s('user', i % cls.n), s('content', i))

    def test_feed_pull(self):
        def check(array):
            buf = 20
            flag = True
            for each in array:
                print('post id: ', each['post_id'], '; buf: ', buf)
                if each['post_id'] != buf:
                    flag = False
                buf -= 1
            return flag

        feeds = user_article.feeds_pull(s('user', 0), 1, 100)
        feeds = json_response2json(feeds)
        self.assertEqual(feeds['status'], 200)
        self.assertTrue(check(array=feeds['data']['feeds']))

    def test_feed_push(self):
        def check(array):
            buf = 20
            flag = True
            for each in array:
                print('post id: ', each['post_id'], '; buf: ', buf)
                if each['post_id'] != buf:
                    flag = False
                buf -= 1
            return flag

        feeds = user_article.get_feeds(s('user', 0), 1, 100)
        feeds = json_response2json(feeds)
        self.assertEqual(feeds['status'], 200)
        self.assertTrue(check(array=feeds['data']['feeds']))

    def test_diff_push_pull(self):
        pull = user_article.feeds_pull(s('user', 0), 1, 100)
        push = user_article.get_feeds(s('user', 0), 1, 100)
        self.assertEqual(pull.content, push.content)

    def test_many2many_reverse_query(self):
        index = 2

        def check(array):
            for each in array:
                if each == User.objects.get(username=s('user', index)):
                    continue
                if each != User.objects.get(username=s('user', 0)):
                    return False
            return True

        __user = User.objects.get(username=s('user', index))
        self.assertTrue(check(array=__user.user_set.all()))


class FavotitesTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='lucien', nickname='lucien', password='password')
        User.objects.create(username='hantiaotiao', nickname='hantiaotiao', password='password')
        User.objects.create(username='neo', nickname='neo', password='password')
        lucien = User.objects.get(username='lucien')
        Article.objects.create(user=lucien, content='I am Lucien Shui!')
        han = User.objects.get(username='hantiaotiao')
        Article.objects.create(user=han, content='I am Hantiaotiao!')
        neo = User.objects.get(username='neo')
        Article.objects.create(user=neo, content='I am Neo!')

    def test_create_favorites(self):
        han = User.objects.get(username='hantiaotiao')
        han.create_favorites(favorites_name='pub_fav', private=False)
        han.create_favorites(favorites_name='pri_fav', private=True)

    def test_add_article(self):
        han = User.objects.get(username='hantiaotiao')
        favorites = han.create_favorites(favorites_name='pub_fav', private=False)
        article = Article.objects.filter().last()
        favorites.add_article(article)
        print(favorites.json(show_articles=True, show_user=True))
        favorites.remove_article(article)
        print(favorites.json(show_articles=True, show_user=True))

    def test_article_in_which_favorites(self):
        article = Article.objects.filter().first()

        han = User.objects.get(username='hantiaotiao')
        pub_favorites = han.create_favorites(favorites_name='pub_fav', private=False)
        pub_favorites.add_article(article)

        pri_favorites = han.create_favorites(favorites_name='pri_fav', private=True)
        pri_favorites.add_article(article)

        print(article.in_which_favorites(han))
        pri_favorites.remove_article(article)
        print(article.in_which_favorites(han))
