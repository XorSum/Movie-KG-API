FROM ubuntu:18.04

ENV PYTHONIOENCODING utf-8

RUN apt update && \
    apt install python3 python3-pip libmysqlclient-dev -y && \
    apt autoremove && \
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple uwsgi

WORKDIR /app

ADD ./requirements.txt /app

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple  -r ./requirements.txt

ADD . /app

EXPOSE 8000

ENTRYPOINT ["uwsgi", "--http", ":8000" ,"--chdir", "./",  "--module", "MovieKgAPI.wsgi"]