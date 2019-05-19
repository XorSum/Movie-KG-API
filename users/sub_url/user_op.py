from django.urls import path
from users import views


urlpatterns = [
    path('log/', views.log, name='user.username.print'),
    path('star/list', views.star_list, name='user.username.star.list'),
    path('star/<str:__username>', views.star, name='user.username.star.username'),
]
