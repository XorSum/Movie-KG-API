#! /bin/bash

MODEL_LIST="rdf users"
for model in ${MODEL_LIST}; do
    rm -rf ${model}/migrations/*
    touch ${model}/migrations/__init__.py
done
rm -f db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate