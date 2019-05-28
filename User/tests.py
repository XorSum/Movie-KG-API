from django.test import TestCase
from User.util import user, user_article, article
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

    def test_favorites(self):
        for i in range(5):
            username = 'user'+str(i)
            user = User.objects.get(username=username)
            article = Article.objects.create(content='article',user=user)
            user.create_favorites('favo'+str(i))
            for i in user.favorites_set.all():
                i.add_article(article)
                print(i.json())
                i.remove_article(article)
                print(i.json())
            print(user.json())