import logging
from urllib import parse

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from Subject.models import Movie, Person
from utils.json_response import json_response


def hello(*args,**kwargs):
    return HttpResponse('congratulations! it works!')


def get_subject(request, subjectId):
    try:
        subject = Person.objects.get(id=subjectId)
        return json_response(subject.json(show_movie=True), 200)
    except ObjectDoesNotExist:
        try:
            subject = Movie.objects.get(id=subjectId)
            return json_response(subject.json(show_person=True), 200)
        except ObjectDoesNotExist:
            return json_response('Subject not found exception', 400)


def search_subject(request):
    try:
        name = request.GET['name']
    except:
        return json_response('need param \'name\'', 500)
    result = []
    for movie in Movie.objects.filter(title=name).all():
        result.append(movie.json(show_person=True))
    for person in Person.objects.filter(name=name).all():
        result.append(person.json(show_movie=True))
    return json_response(result, 200)


def get_movie(request, movieId):
    logging.info('get movie, id=' + str(movieId))
    try:
        movie = Movie.objects.get(id=movieId)
        return json_response(movie.json(show_person=True, show_video=True), 200)
    except Exception as e:
        repr(e)
        return json_response('error', 500)


def get_person(request, personId):
    logging.info('get person, id=' + str(personId))
    try:
        person = Person.objects.get(id=personId)
        return json_response(person.json(show_movie=True), 200)
    except Exception as e:
        return json_response('error', 500)


def search_movie(request):
    result = []
    try:
        title = parse.unquote(request.GET['title'])
        logging.info('search movie, title=' + str(title))
        for movie in Movie.objects.filter(title=title).all():
            result.append(movie.json(show_person=True))
        return json_response(result, 200)
    except:
        return json_response([], 500)


def search_person(request):
    result = []
    try:
        name = parse.unquote(request.GET['name'])
        logging.info('search person, name=' + str(name))
        for person in Person.objects.filter(name=name).all():
            result.append(person.json(show_movie=True))
        return json_response(result, 200)
    except:
        return json_response([], 500)
