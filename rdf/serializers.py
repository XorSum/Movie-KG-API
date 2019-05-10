from django.contrib.auth.models import  Group
from rest_framework import serializers
from .models import MyUser
from rdf.models import Movie


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('url', 'username', 'email', 'groups','abc','friends')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('url','id','name')