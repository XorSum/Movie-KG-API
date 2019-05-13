from django.contrib.auth.models import  Group
from rest_framework import serializers
from .models import MyUser, Article

from rdf.models import Movie


class UserSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True,queryset=Article.objects.all())
    class Meta:
        model = MyUser
        fields = ('url', 'username', 'email', 'groups','abc','friends','articles')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('url','id','name')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer(required=False)
    class Meta:
        model = Article
        fields = ('url','id','content','user','datetime','link')
