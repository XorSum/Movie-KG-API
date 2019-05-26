from django.db import models
from utils.serializer import to_dict

# Create your models here.


class Movie(models.Model):
    id = models.AutoField(verbose_name='编号', primary_key=True, editable=False)
    year = models.IntegerField(verbose_name='年份', blank=True, null=True)
    title = models.CharField(verbose_name='名称', max_length=256, blank=True, null=True)
    rating = models.FloatField(verbose_name='评分', blank=True, null=True)
    summary = models.TextField(verbose_name='简介', blank=True, null=True)
    original_title = models.CharField(verbose_name='原名', max_length=255, blank=True, null=True)

    def __str__(self):
        return "Movie: " + self.title + "-" + str(self.id)

    def serialize(self, show_person=False, show_video=False):
        """
        序列化
        """
        data = to_dict(self, ['id', 'year', 'title', 'rating', 'summary', 'original_title'])
        data['url'] = '/subject/movie/' + str(self.id) + '/'
        data['type'] = 'movie'
        if show_person:
            data['persons'] = [mp.serialize(show_person=True) for mp in MoviePerson.objects.filter(movie=self).all()]
        if show_video:
            data['videos'] = [video.serialize() for video in MovieVideo.objects.filter(movie=self).all()]
        return data


class Person(models.Model):
    id = models.AutoField(verbose_name='编号', primary_key=True, editable=False)
    name = models.CharField(verbose_name='姓名', max_length=256, blank=True, null=True)
    gender = models.CharField(verbose_name='性别', max_length=10, blank=True, null=True)
    name_en = models.CharField(verbose_name='英文姓名', max_length=256, blank=True, null=True)
    summary = models.TextField(verbose_name='简介', blank=True, null=True)
    birthday = models.DateField(verbose_name='生日', blank=True, null=True)
    born_place = models.CharField(verbose_name='出生地', max_length=256, blank=True, null=True)

    def __str__(self):
        return "Person: " + self.name + "-" + str(self.id)

    def serialize(self, show_movie=False):
        data = to_dict(self, ['id', 'name', 'gender', 'name_en', 'summary', 'birthday', 'bornplace'])
        data['url'] = '/subject/person/' + str(self.id) + '/'
        data['type'] = 'person'
        if show_movie:
            data['movies'] = [mp.serialize(show_movie=True) for mp in MoviePerson.objects.filter(person=self).all()]
        return data


class MoviePerson(models.Model):
    role = models.CharField(verbose_name='职务', max_length=10, blank=True, null=True)
    movie = models.ForeignKey(verbose_name='电影', to=Movie, on_delete=models.PROTECT)
    person = models.ForeignKey(verbose_name='人', to=Person, on_delete=models.PROTECT)

    def __str__(self):
        return "Movie Person: " + self.movie.title + " - " + self.person.name + " - " + self.role

    def serialize(self, show_movie=False, show_person=False):
        data = {'role': self.role}
        if show_person:
            data['person'] = self.person.serialize()
        if show_movie:
            data['movie'] = self.movie.serialize()
        return data


class MovieVideo(models.Model):
    movie = models.ForeignKey(verbose_name='电影', to=Movie, on_delete=models.PROTECT)
    sample_link = models.CharField(verbose_name='链接', max_length=256, default='https://baidu.com')
    source = models.CharField(verbose_name='来源', max_length=10, default='自己搜')

    def __str__(self):
        return "Movie Video: " + self.movie.title + " - " + self.sample_link

    def serialize(self):
        data = to_dict(self, ['sample_link', 'source'])
        return data


class MovieTag(models.Model):
    movie = models.ForeignKey(verbose_name='电影', to=Movie, on_delete=models.PROTECT)
    tag = models.CharField(verbose_name='标签', max_length=256)

    def __str__(self):
        return "Movie Video: " + self.movie.title + " - " + self.tag


class MovieGenre(models.Model):
    movie = models.ForeignKey(verbose_name='电影', to=Movie, on_delete=models.PROTECT)
    genre = models.CharField(verbose_name='类型', max_length=256)

    def __str__(self):
        return "Movie Video: " + self.movie.title + " - " + self.genre
