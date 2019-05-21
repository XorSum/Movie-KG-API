
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
POST /api/v1/user/join?username=&nickname=&password=
POST /api/v1/user/login?username=&password=
GET /api/v1/user/<username>/log
GET /api/v1/user/<username>/star/list
GET /api/v1/user/<username>/star/<username>
```

#### Article

```plain
POST /api/v1/user/<username>/publish?content=
GET /api/v1/user/<username>/articles
GET /api/v1/user/<username>/article/<post_id>
```

#### Movie

```plain
GET /api/v1/movie/movie/search/?title=
GET /api/v1/movie/movie/<movieId>/
GET /api/v1/movie/person/search/?name=
GET /api/v1/movie/person/<personId>/
```

#### More

[More details](users/requests.http)


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
CREATRE DATABASE movie_kg CHARACTER SET utf8 COLLATE utf8_general_ci;
```