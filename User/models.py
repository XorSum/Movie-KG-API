from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, username, nickname, password=None):
        """
        Create user in db
        :param username:
        :param nickname:
        :param password:
        :return:
        """
        def valid(__username):
            """
            Check username is valid
            :param __username:
            :return: True / False
            """
            if not __username:
                return False
            if not __username[0].islower():
                return False
            for ch in __username:
                if not (ch.islower() or ch.isdigit()):
                    return False
            return True

        if not valid(username):
            raise ValueError('用户名必须由小写字母和数字组成，且开头为小写字母')

        user = self.model(
            username=username,
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        user.following.add(user)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nickname, password):
        """
        Create a normal user first, then set it administrator
        :param username:
        :param nickname:
        :param password:
        :return:
        """
        user = self.create_user(
            username=username,
            nickname=nickname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(verbose_name='用户名', primary_key=True, editable=False, unique=True, max_length=18)
    nickname = models.CharField(verbose_name='用户昵称', max_length=32)
    is_active = models.BooleanField(verbose_name='用户可用', default=True)
    is_admin = models.BooleanField(verbose_name='管理员用户', default=False)
    article_count = models.IntegerField(default=0, verbose_name='推文数量', editable=False)
    following = models.ManyToManyField("self")

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
        :return:
        """
        self.following.add(followee)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
