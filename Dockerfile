FROM ubuntu:18.04

MAINTAINER hantiaotiao 1779754921@qq.com

RUN apt update && \
    apt install python3 python3-pip libmysqlclient-dev netcat -y && \
    apt autoremove

WORKDIR /app

ADD ./requirements.txt /app

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple  -r ./requirements.txt

ADD . /app

EXPOSE 8000

ENV PYTHONIOENCODING utf-8

ENV DJANGO_SETTINGS_MODULE MovieKgAPI.settings.prod

ENTRYPOINT ["./wait-for.sh", "mysql:3306", "--", "bash","docker-start.sh"]