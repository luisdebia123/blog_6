
from .base import *

DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog_6', 
        'USER' : 'postgres',
        'PASSWORD' :'123321',
        'HOST' : 'localhost',
        'PORT':'5432',
        
    }
}
