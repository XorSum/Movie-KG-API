from django.db import models


class ReadHistory(models.Model):
    """
    某个用户查看某个电影或者人物，则需要加一条记录
    """
    user = models.ForeignKey(to='User.User', on_delete=models.PROTECT)
    movie = models.ForeignKey(to='Subject.Movie', on_delete=models.PROTECT, null=True, blank=True)
    person = models.ForeignKey(to='Subject.Person', on_delete=models.PROTECT, null=True, blank=True)
    read_time = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)