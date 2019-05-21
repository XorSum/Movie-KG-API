from django.urls import path

from movie import views

urlpatterns = [
    path('hello/', views.hello),
    path('movie/search/', views.search_movie),
    path('movie/<int:movieId>/', views.get_movie),
    path('person/search/', views.search_person),
    path('person/<int:personId>/', views.get_person),
]
