from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import PROTECT

from MovieKgAPI import settings


class MyUser(AbstractUser):
    abc = models.CharField(max_length=100,blank=True,null=True)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,null=True)


# class Favorites(models.Model):
#     time = models.DateTimeField()
#     # user = models.OneToOneField('User')


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=2048,blank=True,null=True)
    datetime = models.DateTimeField(blank=True,null=True)
    link = models.CharField(max_length=256,blank=True,null=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=PROTECT, related_name='articles')

