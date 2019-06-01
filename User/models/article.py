from django.db import models

from utils import utils


class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='推文编号', editable=False)
    content = models.CharField(verbose_name='内容', max_length=240)
    created_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    user = models.ForeignKey(verbose_name='发表用户', to='User.User', on_delete=models.PROTECT)
    movie = models.ForeignKey(verbose_name='推荐电影', to='Subject.Movie', on_delete=models.PROTECT, null=True, blank=True)
    person = models.ForeignKey(verbose_name='推荐影人', to='Subject.Person', on_delete=models.PROTECT, null=True,
                               blank=True)

    def json(self):
        data = {
            'article_id': self.id,
            'content': self.content,
            'created_date': self.created_date,
            'user': self.user.username
        }
        if self.movie:
            data['movie'] = self.movie.json(show_all=True)
        else :
            data['movie'] = None
        if self.person:
            data['person'] = self.person.json(show_all=True)
        else:
            data['person'] = None
        return data

    class Meta:
        verbose_name = '动态'
        verbose_name_plural = '动态'
