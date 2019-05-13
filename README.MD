
# 基于知识图谱的问答系统

## 使用

/api/v3/person/?id=1274242
/api/v3/person/?name=黄渤
/api/v3/movie/?id=1291543
/api/v3/movie/?title=功夫


访问 `http://localhost:8000/help/` 查看支持的问题

访问`http://localhost:8000/search/?question=周星驰出演的电影`进行询问

以下get接口均需将参数encodeURIComponent()
```
http://localhost:8000/search/?question=

/getUrl/?name=周星驰
response :  "http://editme.top#movie/9470"

/getName/?url=

/relationFrom/?object=

/relationTo/?subject=
```

subject predicate object  
主      谓         宾


## 测试运行

```
rm */migrations/00001_initial.py
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```


## 部署

安装uwsgi,注意它不是安装在虚拟环境中，而是安装在系统中  
`sudo pip install uwsgi --upgrade`

后台运行  
`nohup uwsgi --http :8000 --chdir ./ --home=./venv  --module MovieKgAPI.wsgi  &`
查看输出  
`tail -f nohup.out`

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