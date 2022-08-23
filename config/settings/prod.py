from distutils.debug import DEBUG
from this import d
import django_on_heroku
from decouple import config

from config.settings.dev import SECRET_KEY

from .base import *

SECRET_KEY = config('SECRET_KEY') 

DEBUG = False

ALLOWED_HOSTS = [
    'ksu-shop-all.herokuapp.com',
    'ksu.shop',
]

DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version':1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple' : {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers':{
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'MYAPP': {
            'handlers': ['console'],
            'level':'DEBUG'
        },
    }
}

#Heroku settings
django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']