FROM ubuntu:18.04

RUN apt update && \
    apt install python3 python3-pip libmysqlclient-dev -y && \
    apt autoremove && \
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple uwsgi

EXPOSE 8000

WORKDIR /app

ADD . /app

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple  -r ./requirements.txt

ENTRYPOINT ["uwsgi", "--http", ":8000" ,"--chdir", "./",  "--module", "MovieKgAPI.wsgi"]