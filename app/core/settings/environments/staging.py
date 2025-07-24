# mypy: ignore-errors

import os

from ..logging import LOGGING

DEBUG = False

SECRET_KEY = os.getenv('STAGING_SECRET_KEY')

ALLOWED_HOSTS = os.getenv('STAGING_ALLOWED_HOSTS').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('STAGING_POSTGRES_DB'),
        'USER': os.getenv('STAGING_POSTGRES_USER'),
        'PASSWORD': os.getenv('STAGING_POSTGRES_PASSWORD'),
        'HOST': os.getenv('STAGING_POSTGRES_HOST'),
        'PORT': os.getenv('STAGING_POSTGRES_PORT')
    }
}

IN_DOCKER = True

LOGGING['handlers']['console']['level'] = os.getenv('STAGING_LOG_LEVEL')
LOGGING['root']['level'] = os.getenv('STAGING_LOG_LEVEL')
for logger_name in LOGGING['loggers']:
    LOGGING['loggers'][logger_name]['level'] = os.getenv('STAGING_LOG_LEVEL')
