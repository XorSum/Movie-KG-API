#!/bin/bash

if [[ $1 == "clean" || $1 == "reset" ]]; then
    MODEL_LIST="rdf User movie"
    for model in ${MODEL_LIST}; do
        rm -rf ${model}/migrations/*
        touch ${model}/migrations/__init__.py
    done
    rm -f db.sqlite3

    if [[ $1 == "reset" ]]; then
        python3 manage.py makemigrations
        python3 manage.py migrate
    fi
else
    echo "Usage: bash migrate.sh <clean|reset>"
fi
