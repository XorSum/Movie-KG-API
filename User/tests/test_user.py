from django.test import TestCase

from User.models import User
from User.service import user_service, article_service

import json

def s(name, i):
    return '%s%s' % (name, i)

# django

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
            user_service.join(username=s('user', i), nickname=s('nick', i), password='test')
        user0 = User.objects.get(username='user0')
        for i in range(1, cls.n):
            user_service.follow(user0, s('user', i))
        for i in range(cls.n << 2):
            useri = User.objects.get(username=s('user', i % cls.n))
            article_service.publish(useri, s('content', i))

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

        user0 = User.objects.get(username=s('user', 0))
        feeds = article_service.get_feeds_slow(user0, 0, 19)
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

        user0 = User.objects.get(username=s('user', 0))
        feeds = article_service.get_feeds_fast(user0, 0, 19)
        feeds = json_response2json(feeds)
        self.assertEqual(feeds['status'], 200)
        self.assertTrue(check(array=feeds['data']['feeds']))


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
