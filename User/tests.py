from django.test import TestCase
from User.util import user, user_article, article
import json


def s(name, i):
    return '%s%s' % (name, i)


def json_response2json(response):
    return json.loads(response.content.decode())


class UserTestCase(TestCase):
    n = 5

    @classmethod
    def setUpTestData(cls):
        for i in range(cls.n):
            user.join(username=s('user', i), nickname=s('nick', i), password='test')
        for i in range(1, cls.n):
            user.follow('user0', s('user', i))
        for i in range(cls.n << 2):
            user_article.publish(s('user', i % cls.n), s('content', i))

    def test_feed_pull(self):
        def check(array):
            buf = 20
            for each in array:
                if each['post_id'] != buf:
                    return False
                return True

        feeds = user_article.feed_pull(s('user', 0), 1, 5)
        feeds = json_response2json(feeds)
        self.assertEqual(feeds['status'], 200)
        self.assertTrue(check(array=feeds['data']['feeds']))
