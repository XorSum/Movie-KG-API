from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField()

    def __str__(self):
        return self.name + "--" + str(self.year)
