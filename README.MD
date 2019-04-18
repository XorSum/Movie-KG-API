
# 基于知识图谱的问答系统

## 使用

访问 `http://localhost:8000/help/` 查看支持的问题

访问`http://localhost:8000/search/?question=周星驰出演的电影`进行询问

```

/getUrl/?name=周星驰
response :  "person/57607"

encodeURIComponent(#)

/relationFrom/?object=person/57607

/relationTo/?subject=movie/55156
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
`nohup uwsgi --http :8000 --chdir ./ --home=./venv  --module KnowGraphAPI.wsgi  &`  
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