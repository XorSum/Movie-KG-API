
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
POST /user/join?username=&nickname=&password=
POST /user/login?username=&password=
GET /user/<username>/log
GET /user/<username>/star/list
GET /user/<username>/star/<username>
```

#### Article

```plain
POST /user/<username>/publish?content=
GET /user/<username>/articles
GET /user/<username>/article/<post_id>
```

#### Movie

```plain
GET /movie/movie/search/?title=
GET /movie/movie/<movieId>/
GET /movie/person/search/?name=
GET /movie/person/<personId>/
```

#### More

[More details](users/requests.http)

#### Deprecated

```plain
/api/v3/person/?id=1274242
/api/v3/person/?name=黄渤
/api/v3/movie/?id=1291543
/api/v3/movie/?title=功夫
------
http://localhost:8000/help/  查看支持的问题
http://localhost:8000/search/?question=周星驰出演的电影  进行询问
http://localhost:8000/search/?question=
/getUrl/?name=周星驰   response:"http://editme.top#movie/9470"
/getName/?url=
/relationFrom/?object=
/relationTo/?subject=
------
subject  predicate  object  
主       谓          宾
```

## 测试运行

```
$ bash ./migrate.sh reset
$ python3 manage.py createsuperuser
$ python3 manage.py runserver
```


## 部署

安装python3,uwsgi等依赖

```bash
$ sudo apt install python3 python3-venv git
$ sudo pip3 install uwsgi
$ sudo apt-get install libmysqlclient-dev
```

启动
```bash
$ bash run.sh
```

查看输出
```bash
$ tail -fn 20 nohup.out
```

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