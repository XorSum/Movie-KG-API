from django.contrib.auth.models import  AbstractUser
from django.db import models


# Create your models here.
from MovieKgAPI import settings


class MyUser(AbstractUser):
    abc = models.CharField(max_length=100)
    # pass
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return "{" + str(self.id) + ":" + str(self.name) + "}"


class Favorites(models.Model):
    time = models.DateTimeField()
    # user = models.OneToOneField('User')


