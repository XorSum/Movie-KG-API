from django.db import models

from utils import utils


class Article(models.Model):
    post_id = models.AutoField(primary_key=True, verbose_name='推文编号', editable=False)
    content = models.CharField(verbose_name='内容', max_length=240)
    created_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    user = models.ForeignKey(verbose_name='发表用户', to='User.User', on_delete=models.PROTECT)
    movie = models.ForeignKey(verbose_name='推荐电影', to='Subject.Movie', on_delete=models.PROTECT, null=True, blank=True)
    person = models.ForeignKey(verbose_name='推荐影人', to='Subject.Person', on_delete=models.PROTECT, null=True,
                               blank=True)

    def json(self):
        return {
            'post_id': self.post_id,
            'content': self.content,
            'date': self.created_date,
            'user': self.user.username,
            'movie': utils.get_json_or_none(self.movie),
            'person': utils.get_json_or_none(self.person)
        }

    class Meta:
        verbose_name = '动态'
        verbose_name_plural = '动态'

    def in_which_favorites(self, user):
        return [each.json() for each in self.favorites_set.filter(user=user).all()]

    def add_to_favorites(self, favorites):
        favorites.add_article(self)

    def remove_from_favorites(self, favorites):
        favorites.remove_article(self)
