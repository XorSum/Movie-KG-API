#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'admin')" | python3 manage.py shell

uwsgi --http :8000 --chdir ./ --module MovieKgAPI.wsgi
