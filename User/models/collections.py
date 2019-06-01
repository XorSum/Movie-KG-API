from django.db import models


class Collection(models.Model):
    id = models.AutoField(verbose_name='收藏夹编号', primary_key=True)
    name = models.CharField(verbose_name='收藏夹名称', max_length=240)
    user = models.ForeignKey(verbose_name='主人', to='User.User', on_delete=models.PROTECT)
    articles = models.ManyToManyField(verbose_name='收藏的文章', to='User.Article')
    private = models.BooleanField(verbose_name='是否为私有')

    class Meta:
        unique_together = ('user', 'name')

    def json(self, show_articles=False, show_user=False):
        result = {'id': self.id,
                  'name': self.name,
                  'private': self.private,
                  'article_count': self.articles.count()}
        if show_articles:
            result['articles'] = [each.json() for each in self.articles.all()]
        if show_user:
            result['user'] = self.user.json()
        return result
