from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'movie_kg',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'POST': 3306,
    }
}
