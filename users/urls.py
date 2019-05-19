from django.urls import path, include
from users import views
from users.sub_url import user_op


urlpatterns = [
    path('login', views.login, name='user.login'),
    path('join', views.join, name='user.join'),
    path('<str:username>/', include(user_op)),
]
