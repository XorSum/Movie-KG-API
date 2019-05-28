from django.db import models

from MovieKgAPI.settings.base import AUTH_USER_MODEL
from User.models.article import Article


class Favorites(models.Model):
    name = models.CharField(max_length=240)
    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.PROTECT)
    articles = models.ManyToManyField(to=Article)

    def json(self):
        return {
            'name': self.name,
            'user': self.user.json(),
            'articles': [each.json() for each in self.articles.all()]
        }

    def add_article(self,article):
        """
        收藏一篇文章
        :param article:
        :return:
        """
        self.articles.add(article)
        return None

    def remove_article(self,article):
        self.articles.remove(article)
        return None