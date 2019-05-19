from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, username, nickname, password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nickname, password):
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
    stars = models.ManyToManyField("self")

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Article(models.Model):
    post_id = models.IntegerField(primary_key=True, verbose_name='推文编号', editable=False)
    content = models.CharField(verbose_name='内容', max_length=240)
    created_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='发表用户', on_delete=models.PROTECT)

    class Meta:
        verbose_name = '动态'
        verbose_name_plural = '动态'
