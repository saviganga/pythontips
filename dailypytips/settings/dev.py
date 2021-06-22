from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}