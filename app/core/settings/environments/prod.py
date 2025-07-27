# mypy: ignore-errors

import os

from ..logging import LOGGING
from .base import SIMPLE_JWT

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

# Configurações de autenticação via Token JWT
SIMPLE_JWT.update({
    'SIGNING_KEY ': SECRET_KEY,
    'ALGORITHM': 'HS256',
    'UPDATE_LAST_LOGIN': True,
})

# Configurações de segurança

CSRF_TRUSTED_ORIGINS = [f"https://{host.strip()}" for host in ALLOWED_HOSTS]

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = 'DENY'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_HSTS_SECONDS = 31536000  # 1 ano
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

CORS_ALLOWED_ORIGINS = [f"https://{host.strip()}" for host in ALLOWED_HOSTS]

LOGGING['handlers']['console']['level'] = os.getenv('PROD_LOG_LEVEL')
LOGGING['root']['level'] = os.getenv('PROD_LOG_LEVEL')
for logger_name in LOGGING['loggers']:
    LOGGING['loggers'][logger_name]['level'] = os.getenv('PROD_LOG_LEVEL')
