from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from User.models.usermanager import UserManager


class User(AbstractBaseUser):
    username = models.CharField(verbose_name='用户名', primary_key=True, editable=False, unique=True, max_length=18)
    nickname = models.CharField(verbose_name='用户昵称', max_length=32)
    is_active = models.BooleanField(verbose_name='用户可用', default=True)
    is_admin = models.BooleanField(verbose_name='管理员用户', default=False)
    following = models.ManyToManyField('User.User', verbose_name="我关注的人")
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
            'article_count': self.article_set.count()
        }

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
