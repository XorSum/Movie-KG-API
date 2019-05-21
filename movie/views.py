from urllib import parse
from django.http import HttpResponse
from movie.models import Movie, Person
from utils.json_response import json_response


def hello(request):
    return HttpResponse('app movie works!')


def get_movie(request, movieId):
    try:
        movie = Movie.objects.get(id=movieId)
        print(movie)
        return json_response(movie.serialize(show_person=True, show_video=True), 200)
    except Exception as e:
        repr(e)
        return json_response('error', 500)


def get_person(request, personId):
    try:
        person = Person.objects.get(id=personId)
        print(person)
        return json_response(person.serialize(show_movie=True), 200)
    except Exception as e:
        return json_response('error', 500)


def search_movie(request):
    result = []
    try:
        title = parse.unquote(request.GET['title'])
        print(title)
        for movie in Movie.objects.filter(title=title).all():
            result.append(movie.serialize(show_person=True))
        return json_response(result, 200)
    except:
        return json_response([], 500)


def search_person(request):
    result = []
    try:
        name = parse.unquote(request.GET['name'])
        for person in Person.objects.filter(name=name).all():
            result.append(person.serialize(show_movie=True))
        return json_response(result, 200)
    except:
        return json_response([], 500)
