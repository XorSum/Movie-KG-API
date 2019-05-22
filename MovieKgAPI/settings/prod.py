from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.setdefault('MYSQL_DATABASE', 'movie_kg'),
        'USER':  os.environ.setdefault('MYSQL_USERNAME', 'root'),
        'PASSWORD':  os.environ.setdefault('MYSQL_PASSWORD', '123456'),
        'HOST':  os.environ.setdefault('MYSQL_HOST', '127.0.0.1'),
        'PORT':  os.environ.setdefault('MYSQL_PORT', '3306'),
    }
}
