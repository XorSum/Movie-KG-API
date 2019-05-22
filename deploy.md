## 部署

这份文档记录了如何在一台ubuntu 18.04服务器上的部署整个项目的过程

首先是一些准备工作，比如下载安装各种软件:
```
sudo apt install git vim python3 python3-venv  mysql-server libmysqlclient-dev nginx
sudo pip3 install uwsgi
```
假设我们的项目放在`/homw/wwwroot/`目录下
后端代码在`/home/wwwroot/Movie-KG/api/`，
前端编译出的静态代码在`/home/wwwroot/Movie-KG/static/`

创建这些文件夹
```
mkdir /home/wwwroot /home/wwwroot/Movie-KG/
cd /home/wwwroot/Movie-KG/
mkdir static
```
然后下载源代码
```
git clone https://github.com/XorSum/Movie-KG-API.git api
cd api
```

现在我们在后端代码中搞事情

设置一个环境变量
```bash
export DJANGO_SETTINGS_MODULE=MovieKgAPI.settings.prod
```

`/home/wwwroot/Movie-KG/api/MovieKgAPI/settings.py`这个文件是后端的配置文件，其中记录着数据库配置等各种信息.
你可以在其中找到某一行写着`STATIC_ROOT ='/home/wwwroot/Movie-KG/static/static/'`,这是稍后生成django admin所需的静态文件的目标地址，
如果你没有跟我一样使用`/home/wwwroot/Movie-KG/`目录，而是其它的奇奇怪怪的目录的话，那么你就需要修改这一行了。

创建一个python的虚拟环境
```bash
python3 -m venv venv
source ./venv/bin/activate
```
成功之后你会发现命令提示符前面多了个`(venv)`

然后安装各种库
```bash
pip install -r requirements.txt
```

前面提到过生成静态文件，现在开始：
```bash
python3 manage.py collectstatic
```
这一步完成后，会出现一个`/home/wwwroot/Movie-KG/static/static/admin/`目录，这个目录中有css,fonts,img,js等目录

接下来我们开始进行迁移数据库。虽然本文档前面写着安装mysql,但是截止目前为止这个项目仍然使用的是sqlite3。

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```

如果你是在本地运行的话，到这一步就可以运行`python3 manage.py runserver`命令开启一个测试用的server，
然后在浏览器中访问[localhost:8000/admin/](localhost:8000/admin/)管理控制台，
或者[localhost:8000/admin/doc/](localhost:8000/admin/doc/)文档。

如果是部署于服务器，那么我们需要通过uwsgi开启一个稳定的server。
```bash
uwsgi --http :8000 --chdir ./ --home=./venv  --module MovieKgAPI.wsgi
```
然而这时你打开admin页面就会发现，css文件竟然没了！我们需要通过nginx来解决这一问题。

```bash
sudo vim /etc/nginx/conf.d/moviekg.conf
```
在这个文件中填写如下内容：
```plain
server {
   listen       9000;
   server_name  Movie-KG;
   root /home/wwwroot/Movie-KG/static; 
   index index.html;
   location / {
       try_files $uri $uri/ /index.html;
   }
   location /admin {
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header REMOTE-HOST $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://localhost:8000/admin;
    }
}
```
重启nginx服务
```bash
sudo systemctl restart nginx
```

这时在浏览器中访问[localhost:9000/admin/](localhost:9000/admin/)，admin页面的css文件加载出来了。

----

to be continued

