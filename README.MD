
# 基于知识图谱的问答系统

## API

get接口中的参数值如果是汉字，则需要将其encodeURIComponent()

#### Admin

```plain
/admin/  django控制台
/admin/doc/  django文档
```

#### User

```plain
# 主动的操作
GET /api/v1//v1/login/    # POST  params: username, password
GET /api/v1//v1/join/    # POST    params: username, nickname, password
GET /api/v1//v1/article/    # 发表文章 POST   params: contend , movieId, personId, token
GET /api/v1//v1/feeds/    # 获取feeds GET   params: start, end, token
GET /api/v1//v1/follow/<str:followee>/

# 旁观者的视角
GET /api/v1//v1/user/<username>/articles/    # 获取某人的文章 GET params: username
GET /api/v1//v1/user/<username>/public_favorites/    # 获取某人的公开收藏夹列表 GET params: username
GET /api/v1//v1/user/<str:username>/favorites/<int:favorite_id>/   # 获取某人的某个收藏夹中的文章 GET params: usename, favorite_id,
GET /api/v1//v1/user/<str:username>/followers/    # 获取某人的追随者, GET , params: username
GET /api/v1//v1/user/<str:username>/idols/    # 获取某人追随的人, GET , params: username
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

#### More

[More details](User/api_tests/requests.http)


## 测试运行

```
$ bash ./migrate.sh reset
$ python3 manage.py createsuperuser
$ python3 manage.py runserver
```


## 部署

详见[deploy.md](deploy.md)

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

