
# 基于知识图谱的问答系统

## 使用

访问 `http://localhost:8000/help/` 查看支持的问题

访问`http://localhost:8000/search/?q=周星驰出演的电影`进行询问

## 测试运行

```
rm */migrations/00001_initial.py
python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver
```


## 部署

``` 
uwsgi --http :8001 --chdir ./ --home=./venv  --module KnowGraphAPI.wsgi
```