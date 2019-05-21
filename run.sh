#! /bin/bash

port=8001

git pull
if [ ! -d "./venv" ]; then
	python3 -m venv venv
fi
source ./venv/bin/activate
pip install -r requirements.txt
kill -9 $(lsof -ti tcp:$port)
nohup uwsgi --http :$port --chdir ./ --home=./venv  --module MovieKgAPI.wsgi  &

echo -e  "\033[33mthe project started, you can run \"tail -fn 20  nohup.out\" to follow the log\033[0m"


