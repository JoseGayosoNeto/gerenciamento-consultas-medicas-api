# mypy: ignore-errors

import os

from ..logging import LOGGING
from .base import BASE_DIR

SECRET_KEY = os.getenv(
    'DEV_SECRET_KEY',
    'django-insecure-c^4axmu@4n0ca*$a8fx3#a23$@8-!kg^o-l*@i7+vpbo%$eg9k',
)

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

IN_DOCKER = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOGGING['handlers']['console']['level'] = os.getenv('DEV_LOG_LEVEL')
LOGGING['root']['level'] = os.getenv('DEV_LOG_LEVEL')
for logger_name in LOGGING['loggers']:
    LOGGING['loggers'][logger_name]['level'] = os.getenv('DEV_LOG_LEVEL')
LOGGING['root']['handlers'] = [
    'console',
]
