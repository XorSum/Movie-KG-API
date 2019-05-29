from django.db import models


class ReadHistory(models.Model):
    """
    某个用户查看某个电影或者人物，则需要加一条记录
    """
    id = models.AutoField(verbose_name='历史记录编号', primary_key=True)
    user = models.ForeignKey(verbose_name='用户', to='User.User', on_delete=models.PROTECT)
    article = models.ForeignKey(verbose_name='文章', to='User.Article', on_delete=models.PROTECT, null=True, blank=True)
    read_time = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)

    def json(self):
        return {
            'user': self.user.json(),
            'article': self.article.json(),
            'read_time': self.read_time
        }
