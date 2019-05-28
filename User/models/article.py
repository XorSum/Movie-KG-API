from django.db import models

from utils import utils


class Article(models.Model):
    post_id = models.AutoField(primary_key=True, verbose_name='推文编号', editable=False)
    content = models.CharField(verbose_name='内容', max_length=240)
    created_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    user = models.ForeignKey(to='User.User', verbose_name='发表用户', on_delete=models.PROTECT)
    movie = models.ForeignKey(to='Subject.Movie', on_delete=models.PROTECT, null=True, blank=True)
    person = models.ForeignKey(to='Subject.Person', on_delete=models.PROTECT, null=True, blank=True)

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
