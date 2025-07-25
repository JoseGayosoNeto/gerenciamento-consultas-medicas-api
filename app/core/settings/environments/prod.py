# mypy: ignore-errors

import os

from ..logging import LOGGING

DEBUG = False

SECRET_KEY = os.getenv('PROD_SECRET_KEY')

ALLOWED_HOSTS = os.getenv('PROD_ALLOWED_HOSTS').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PROD_POSTGRES_DB'),
        'USER': os.getenv('PROD_POSTGRES_USER'),
        'PASSWORD': os.getenv('PROD_POSTGRES_PASSWORD'),
        'HOST': os.getenv('PROD_POSTGRES_HOST'),
        'PORT': os.getenv('PROD_POSTGRES_PORT')
    }
}

IN_DOCKER = True

LOGGING['handlers']['console']['level'] = os.getenv('PROD_LOG_LEVEL')
LOGGING['root']['level'] = os.getenv('PROD_LOG_LEVEL')
for logger_name in LOGGING['loggers']:
    LOGGING['loggers'][logger_name]['level'] = os.getenv('PROD_LOG_LEVEL')
