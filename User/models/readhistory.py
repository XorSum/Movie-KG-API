from django.db import models

from MovieKgAPI.settings.base import AUTH_USER_MODEL
from Subject.models import Movie, Person


class ReadHistory(models.Model):
    """
    某个用户查看某个电影或者人物，则需要加一条记录
    """
    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.PROTECT)
    movie = models.ForeignKey(to=Movie, on_delete=models.PROTECT, null=True, blank=True)
    person = models.ForeignKey(to=Person, on_delete=models.PROTECT, null=True, blank=True)
    read_time = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)