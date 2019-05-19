from django.urls import path
from users import views


urlpatterns = [
    path('login', views.login, name='user.login'),
    path('join', views.join, name='user.join'),
]
