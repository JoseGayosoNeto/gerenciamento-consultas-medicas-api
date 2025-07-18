import os

from ..logging import LOGGING

DEBUG = False

# ALLOWED_HOSTS: = ['*']

IN_DOCKER = True

LOGGING['handlers']['console']['level'] = os.getenv('PROD_LOG_LEVEL')
LOGGING['root']['level'] = os.getenv('PROD_LOG_LEVEL')
for logger_name in LOGGING['loggers']:
    LOGGING['loggers'][logger_name]['level'] = os.getenv('PROD_LOG_LEVEL')
