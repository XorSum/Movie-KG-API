from datetime import date
from django.test import TestCase
from Subject.models import Movie, Person, MoviePerson
from Subject.views import search_movie


class SubjectTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        movie = Movie.objects.get_or_create(year=2019, title="神奇五合一", rating=10.0,
                                            summary="年度大戏", original_title="神奇五合一")[0]
        person = Person.objects.get_or_create(name="han", gender="男", name_en="han",
                                              summary="一个人", birthday=date.today(), born_place="fc")[0]
        MoviePerson.objects.create(movie=movie, person=person, role='主演')

    def test_json(self):
        movie = Movie.objects.get(title="神奇五合一")
        print(movie.json(show_all=True))
        person = Person.objects.get(name="han")
        print(person.json(show_all=True))
