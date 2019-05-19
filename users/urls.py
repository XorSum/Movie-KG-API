from django.urls import path, include
from users import views
from users.operation import op_urls


urlpatterns = [
    path('login', views.login, name='user.login'),
    path('join', views.join, name='user.join'),
    path('<str:username>/', include(op_urls)),
]
