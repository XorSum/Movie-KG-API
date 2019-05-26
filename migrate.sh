#!/bin/bash

if [[ $1 == "clean" || $1 == "reset" ]]; then
    MODEL_LIST="rdf User Subject"
    for model in ${MODEL_LIST}; do
        rm -rf ${model}/migrations/*
        touch ${model}/migrations/__init__.py
    done
    rm -f db.sqlite3

    if [[ $1 == "reset" ]]; then
        python3 manage.py makemigrations
        python3 manage.py migrate
        echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'admin')" | python3 manage.py shell
    fi
else
    echo "Usage: bash migrate.sh <clean|reset>"
fi
