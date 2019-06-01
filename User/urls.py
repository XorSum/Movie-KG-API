from django.urls import path
import User.views.article_views
import User.views.collection_views
import User.views.user_views

urlpatterns = [

    path('login/', User.views.user_views.user_login, name='api.login'),
    # POST  params: username, password
    path('join/', User.views.user_views.user_join, name='api.join'),
    # POST    params: username, nickname, password

    path('follow/<str:followee_name>/', User.views.user_views.follow, name='api.follow'),
    # POST 关注某人　params: token, followee_name
    path('unfollow/<str:followee_name>/', User.views.user_views.unfollow, name='api.follow'),
    # POST 取关某人　params: token, followee_name
    path('user/<str:username>/followees/', User.views.user_views.user_list_followees),   # pagable
    # 获取追随某人的人, GET , params: username, start, end
    path('user/<str:username>/followees/', User.views.user_views.user_list_followers), # pagable
    # 获取某人追随的人, GET , params: username, start, end

    path('feeds/', User.views.article_views.user_pull_feeds),  # pagable
    # 获取feeds GET   params: token, start, end
    path('article/', User.views.article_views.user_publish_article),
    # 发表文章 POST   params: content , token, 可选参数: article_id,person_id
    path('user/<username>/articles/', User.views.article_views.user_list_article),  # pagable
    # 获取某人的文章 GET params: username, start, end

    path('collection/', User.views.collection_views.user_create_collection),
    # 创建收藏夹  POST   params: name,private, token
    path('collections/', User.views.collection_views.user_list_all_collection),
    # 获取自己的所有的收藏夹列表 GET params: token
    path('user/<str:username>/collections/', User.views.collection_views.user_list_public_collection),
    # 获取某人公开的收藏夹列表 GET params: token
    path('collection/<int:collection_id>/', User.views.collection_views.collection_list_article),  # pagable
    # 获取某个收藏夹中的文章 GET params: collection_id,token, start, end
    path('article/<int:article_id>/which_collections/', User.views.collection_views.article_in_which_collections),
    # 查看某文章被我收藏在哪些收藏夹里 GET, params: article_id, token
    path('article/<int:article_id>/collect/<int:collection_id>/', User.views.collection_views.collection_add_article),
    # 收藏文章 POST params: article_id, collection_id, token
    path('article/<int:article_id>/uncollect/<int:collection_id>/',
         User.views.collection_views.collection_delete_article),
    # 取消收藏文章 DELETE params: article_id, collection_id, token

    path('read/<int:article_id>/', User.views.article_views.user_read_article),
    # 增加阅读记录 POST ,params: article_id, token
    path('history/', User.views.article_views.user_history_article),  # pagable
    # 获取我的阅读记录 GET ,params:  token, start, end

]
