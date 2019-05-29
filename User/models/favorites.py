from django.db import models

from MovieKgAPI.settings.base import AUTH_USER_MODEL
from User.models.article import Article


class Favorites(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=240)
    user = models.ForeignKey(to='User.User', on_delete=models.PROTECT)
    articles = models.ManyToManyField(to='User.Article')
    private = models.BooleanField()

    class Meta:
        unique_together=('user','name')

    def json(self,show_articles=False,show_user=False):
        result = {'name': self.name,
                  'private':self.private}
        if show_articles:
            result['articles'] = [each.json() for each in self.articles.all()]
        if show_user:
            result['user'] = self.user.json()
        return result

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

    def get_articles(self):
        return self.json()