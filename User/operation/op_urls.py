from django.urls import path
from User import views

urlpatterns = [
    path('log/', views.log, name='user.username.print'),
    path('star/list', views.star_list, name='user.username.star.list'),
    path('star/<str:__username>', views.star, name='user.username.star.username'),
    path('publish', views.publish, name='user.username.publish'),
    path('articles', views.article_list, name='user.username.articles'),
    path('article/<int:post_id>', views.view_article, name='user.username.view_article.post_id'),
    path('feeds', views.feed_pull, name='user.username.feed_pull'),
]
