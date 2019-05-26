from django.db import models

from Subject.models import Movie, Person
from User.models import User


class Article(models.Model):
    post_id = models.AutoField(primary_key=True, verbose_name='推文编号', editable=False)
    content = models.CharField(verbose_name='内容', max_length=240)
    created_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='发表用户', on_delete=models.PROTECT)
    movie = models.ForeignKey(to=Movie, on_delete=models.PROTECT,null=True,blank=True)
    person = models.ForeignKey(to=Person, on_delete=models.PROTECT,null=True,blank=True)

    class Meta:
        verbose_name = '动态'
        verbose_name_plural = '动态'


class ReadHistory(models.Model):
    """
    某个用户查看某个电影或者人物，则需要加一条记录
    """

    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    movie = models.ForeignKey(to=Movie, on_delete=models.PROTECT,null=True,blank=True)
    person = models.ForeignKey(to=Person, on_delete=models.PROTECT,null=True,blank=True)
    read_time = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)