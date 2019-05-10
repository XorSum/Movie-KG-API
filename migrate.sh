#! /bin/bash

rm -rf ./rdf/migrations/*
rm ./db.sqlite3
touch ./rdf/migrations/__init__.py
./manage.py makemigrations
./manage.py migrate