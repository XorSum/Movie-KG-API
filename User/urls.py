from django.urls import path
from Subject.views import hello
from User import views


urlpatterns = [

    # 主动的操作
    path('login/', views.login, name='api.login'),  # POST  params: username, password
    path('join/', views.join, name='api.join'),  # POST    params: username, nickname, password
    path('article/', views.publish),  # 发表文章 POST   params: content , token
    path('article/<int:post_id>/favorites/', views.in_which_favorites),  # 查看某文章被我收藏在哪些收藏夹里 GET, params: article_id, token
    path('article/<int:post_id>/favorite/<int:favorites_id>/', views.add_favorites),  # 收藏文章 POST params: article_id, favorites_id, token
    path('article/<int:post_id>/unfavorite/<int:favorites_id>/', views.delete_favorites),  # 取消收藏文章 DELETE params: article_id, favorites_id, token
    path('favorites/', views.create_favorites),  # 创建收藏夹  POST   params: name, token
    path('feeds/', views.feed_pull),  # 获取feeds GET   params: start, end, token
    path('read/', hello),  # 增加阅读记录 POST ,params: article_id, token
    path('history/', hello),  # 获取我的阅读记录 GET ,params:  token
    path('follow/<str:followee_name>/', views.follow, name='api.follow'),

    # 旁观者的视角
    path('user/<username>/articles/', views.get_article_list),  # 获取某人的文章 GET params: username
    path('user/<username>/public_favorites/', views.get_public_favorites),  # 获取某人的公开收藏夹列表 GET params: username
    path('user/<str:username>/favorites/<int:favorite_id>/', views.get_favorites), # 获取某人的某个收藏夹中的文章 GET params: usename, favorite_id,
    path('user/<str:username>/followers/', views.get_followers),  # 获取某人的追随者, GET , params: username
    path('user/<str:username>/idols/', views.get_idols),  # 获取某人追随的人, GET , params: username
]
