from django.contrib import admin
from Subject.models import Movie, Person, MoviePerson, MovieVideo, MovieTag, MovieGenre

# Register your models here.

admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(MoviePerson)
admin.site.register(MovieVideo)
admin.site.register(MovieTag)
admin.site.register(MovieGenre)


