from .base import *

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': dotenv.get('DB_NAME'),
        'USER': dotenv.get('DB_USER', ''),
        'PASSWORD': dotenv.get('DB_PASSWORD', ''),
        'HOST': '127.0.0.1',
        'PORT': dotenv.get('DB_PORT', '5432'),
    }
}
