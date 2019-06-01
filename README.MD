
# 基于知识图谱的问答系统

## API

#### Admin

```plain
/admin/  django控制台
/admin/doc/  django文档
```

#### User

```plain
api/v1/login/ 
# POST  params: username, password
api/v1/join/ 
# POST    params: username, nickname, password

api/v1/follow/<str:followee_name>/ 
# POST 关注某人　params: token, followee_name
api/v1/unfollow/<str:followee_name>/ 
# POST 取关某人　params: token, followee_name
api/v1/user/<str:username>/followees/ 
# 获取追随某人的人, GET , params: username, start, end
api/v1/user/<str:username>/followees/ 
# 获取某人追随的人, GET , params: username, start, end

api/v1/feeds/ 
# 获取feeds GET   params: token, start, end
api/v1/article/ 
# 发表文章 POST   params: content , token, 可选参数: article_id,person_id
api/v1/user/<username>/articles/ 
# 获取某人的文章 GET params: username, start, end

api/v1/collection/ 
# 创建收藏夹  POST   params: name,private, token
api/v1/collections/ 
# 获取自己的所有的收藏夹列表 GET params: token
api/v1/user/<str:username>/collections/ 
# 获取某人公开的收藏夹列表 GET params: token
api/v1/collection/<int:collection_id>/ 
# 获取某个收藏夹中的文章 GET params: collection_id,token, start, end
api/v1/article/<int:article_id>/which_collections/ 
# 查看某文章被我收藏在哪些收藏夹里 GET, params: article_id, token
api/v1/article/<int:article_id>/collect/<int:collection_id>/ 
# 收藏文章 POST params: article_id, collection_id, token
api/v1/article/<int:article_id>/uncollect/<int:collection_id>/ 
     User.views.collection_views.collection_delete_article),
# 取消收藏文章 DELETE params: article_id, collection_id, token

api/v1/read/<int:article_id>/ 
# 增加阅读记录 POST ,params: article_id, token
api/v1/history/ 
# 获取我的阅读记录 GET ,params:  token, start, end
    
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

