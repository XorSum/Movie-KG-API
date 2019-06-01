
# 基于知识图谱的问答系统

## API

#### Admin

```plain
/admin/  django控制台
/admin/doc/  django文档
```

#### User

```plain
path('login/', User.views.user_views.user_login, name='api.login'),
# POST  params: username, password
path('join/', User.views.user_views.user_join, name='api.join'),
# POST    params: username, nickname, password

path('follow/<str:followee_name>/', User.views.user_views.follow, name='api.follow'),
# POST 关注某人　params: token, followee_name
path('unfollow/<str:followee_name>/', User.views.user_views.unfollow, name='api.follow'),
# POST 取关某人　params: token, followee_name
path('user/<str:username>/followees/', User.views.user_views.user_list_followees),
# 获取追随某人的人, GET , params: username
path('user/<str:username>/followees/', User.views.user_views.user_list_followers),
# 获取某人追随的人, GET , params: username

path('feeds/', User.views.article_views.user_pull_feeds),
# 获取feeds GET   params: token, lower,upper
path('article/', User.views.article_views.user_publish_article),
# 发表文章 POST   params: content , token
path('user/<username>/articles/', User.views.article_views.user_list_article),
# 获取某人的文章 GET params: username,lower,upper

path('collection/', User.views.collection_views.user_create_collection),
# 创建收藏夹  POST   params: name,private, token
path('collections/', User.views.collection_views.user_list_all_collection),
# 获取自己的所有的收藏夹列表 GET params: token
path('user/<str:username>/collections/', User.views.collection_views.user_list_public_collection),
# 获取某人公开的收藏夹列表 GET params: token
path('collection/<int:collection_id>/', User.views.collection_views.collection_list_article),
# 获取某个收藏夹中的文章 GET params: collection_id,token
path('article/<int:article_id>/which_collections/', User.views.collection_views.article_in_which_collections),
# 查看某文章被我收藏在哪些收藏夹里 GET, params: article_id, token
path('article/<int:article_id>/collect/<int:collection_id>/', User.views.collection_views.collection_add_article),
# 收藏文章 POST params: article_id, collection_id, token
path('article/<int:article_id>/uncollect/<int:collection_id>/',
     User.views.collection_views.collection_delete_article),
# 取消收藏文章 DELETE params: article_id, collection_id, token

path('read/<int:article_id>/', User.views.article_views.user_read_article),
# 增加阅读记录 POST ,params: article_id, token
path('history/', User.views.article_views.user_history_article),
# 获取我的阅读记录 GET ,params:  token
    
```

#### Subject

```plain
GET /api/v1/subject/search/?name=
GET /api/v1/subject/<subjectId>/
GET /api/v1/subject/movie/search/?title=
GET /api/v1/subject/movie/<movieId>/
GET /api/v1/subject/person/search/?name=
GET /api/v1/subject/person/<personId>/
```
you can consider subject as the abstract class of movie and person.



## 常用命令

### vnev

创建虚拟环境  
`python3 -m venv venv`  
启动虚拟环境  
`source venv/bin/activate`  
退出虚拟环境  
`deactivate`


### requirements.txt

生成requirements.txt文件  
`pip freeze > requirements.txt`  
安装requirements.txt依赖  
`pip install -r requirements.txt`  

### mysql建库
```mysql
CREATE DATABASE movie_kg CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 多settings文件

不同的settings文件用于不同的环境，MovieKgAPI.settings.dev.py用于开发，MovieKgAPI.settings.prod.py用于生产。
django会根据DJANGO_SETTINGS_MODULE这个环境变量来加载相应的settings文件，
阅读[manage.py](./manag.py)中的代码可知，如果没有设置DJANGO_SETTINGS_MODULE，它的默认值是MovieKgAPI.settings.dev。
我们可以在shell中运行`export DJANGO_SETTINGS_MODULE=MovieKgAPI.settings.prod`来设置这个环境变量。
也可以用`python manage.py migrate --settings=MovieKgAPI.settings.prod`的方式来指定环境变量。

### 单元测试

```bash
python3 manage.py test
coverage run --source '.'   manage.py test -v 2 --settings=MovieKgAPI.settings.dev
coverage html
```

打开 htmlcov/index.html

