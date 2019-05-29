from django.urls import path, include
from User import views
from User.operation import user_urls

urlpatterns = [
    path('login', views.login, name='user.login'),
    path('join', views.join, name='user.join'),
    path('<str:username>/', include(user_urls)),
]
