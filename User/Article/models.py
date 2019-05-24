from django.db import models
from User.models import User


class Article(models.Model):
    post_id = models.IntegerField(primary_key=True, verbose_name='推文编号', editable=False)
    content = models.CharField(verbose_name='内容', max_length=240)
    created_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='发表用户', on_delete=models.PROTECT)

    class Meta:
        verbose_name = '动态'
        verbose_name_plural = '动态'
