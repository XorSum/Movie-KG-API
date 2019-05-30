from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from User.models.favorites import Favorites
from User.models.readhistory import ReadHistory
from User.models.usermanager import UserManager
from User.models.article import Article
from utils.JWT import encode


class User(AbstractBaseUser):
    username = models.CharField(verbose_name='用户名', primary_key=True, editable=False, unique=True, max_length=18)
    nickname = models.CharField(verbose_name='用户昵称', max_length=32)
    is_active = models.BooleanField(verbose_name='用户可用', default=True)
    is_admin = models.BooleanField(verbose_name='管理员用户', default=False)
    article_count = models.IntegerField(default=0, verbose_name='推文数量', editable=False)
    following = models.ManyToManyField('User.User', verbose_name="关注者")
    feeds = models.ManyToManyField('User.Article', related_name="feeds", verbose_name="feeds")

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def json(self):
        """
        :return: self's data in JSON
        """
        return {
            'username': self.username,
            'nickname': self.nickname,
            'article_count': self.article_count
        }

    def token(self):
        return encode(self)

    def idol_list(self):
        """
        返回关注的人的列表
        :return:
        """
        ret = []
        for each in User.objects.filter(following=self).all():
            ret.append(each.json())
        return ret


    def follow_list(self):
        """
        :return: self's follow list in JSON
        """
        ret = []
        for each in self.following.all():
            ret.append(each.json())
        return ret

    def follow(self, followee):
        """
        self follow followee
        :param followee:
        :return: None
        """
        self.following.add(followee)

    def publish(self, content):
        """
        Publish an article
        :param content:
        :return: None
        """
        article = Article.objects.create(content=content, user=self)
        self.article_count += 1
        self.save()
        followers = self.user_set.all()
        for each in followers:
            each.feeds.add(article)

    def get_feeds(self, lower, upper):
        """
        get self's feed of [lower, upper]
        :param lower:
        :param upper:
        :return: Query set
        """
        return self.feeds.all().order_by('-created_date')[lower - 1: upper]

    def article_list(self):
        """
        Self's article list sorted by time, minimal index for newest article
        :return: Array
        """
        buf = Article.objects.filter(user=self).order_by('-created_date')
        return [each.json() for each in buf]

    def read(self, article):
        """
        增加一条阅读记录
        :param article:
        :return: None
        """
        ReadHistory.objects.create(user=self, article=article)
        return None

    def read_history(self):
        """
        获取阅读历史
        :return: list of ReadHistories
        """
        buf = ReadHistory.objects.filter(user=self)
        return [each.json() for each in buf]

    def create_favorites(self, favorites_name, private):
        """
        创建收藏夹
        :param favorites_name:
        :return: Favorite对象
        """
        Favorites.objects.create(user=self, name=favorites_name, private=private)
        return self.favorites_set.filter(name=favorites_name).first()

    def get_favorites_list(self):
        """
        获取收藏夹列表
        :return: list of json
        """
        return [each.json() for each in self.favorites_set.all()]

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
