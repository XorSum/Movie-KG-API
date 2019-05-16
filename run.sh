#! /bin/bash

port=8001

git pull
pip install -r requirements.txt
kill -9 $(lsof -ti tcp:$port)
nohup uwsgi --http :$port --chdir ./ --home=./venv  --module MovieKgAPI.wsgi  &
