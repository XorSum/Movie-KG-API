from django.urls import path

from Subject.views import hello

urlpatterns = [

    # 主动的操作
    path('login/', hello),  # POST  params: username, password
    path('join/', hello),  # POST    params: username, nickname, password
    path('article/', hello),  # 发表文章 POST   params: contend , movieId, personId, token
    path('article/<int:article_id>/favorites/', hello),  # 查看某文章被我收藏在哪些收藏夹里 GET, params: article_id, token
    path('favorites/<int:favorites_id>/', hello),  # 收藏文章 POST params: article_id, favorites_id, token
    path('favorites/<int:favorites_id>/', hello),  # 取消收藏文章 DELETE params: article_id, favorites_id, token
    path('favorites/', hello),  # 创建收藏夹  POST   params: name, token
    path('feeds/', hello),  # 获取feeds GET   params: start, end, token
    path('read/', hello),  # 增加阅读记录 POST ,params: article_id, token
    path('history/', hello),  # 获取我的阅读记录 GET ,params:  token

    # 旁观者的视角
    path('user/<str:username>/articles/', hello),  # 获取某人的文章 GET params: username
    path('user/<str:username>/public_favorites/', hello),  # 获取某人的公开收藏夹列表 GET params: username
    path('user/<str:username>/favorites/', hello),  # 获取某人的某个收藏夹中的文章 GET params: usename, favorite_id,
    path('user/<str:username>/followers/', hello),  # 获取某人的追随者, GET , params: username
    path('user/<str:username>/idols/', hello),  # 获取某人追随的人, GET , params: username
]
