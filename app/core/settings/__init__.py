import os

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

load_dotenv()

ENVS = ['DEV', 'PROD', 'STAGING']

env = os.getenv('ENV')
if env not in ENVS:
    raise ImproperlyConfigured(
        f'O valor atual de ENV é {env}, mas ele deve ser um dos \
                                seguintes valores permitidos: {ENVS}'
    )

from .environments.base import *
from .logging import *

match env:
    case 'DEV':
        from .environments.dev import *
    case 'PROD':
        from .environments.prod import *
    case 'STAGING':
        from .environments.staging import *

if IN_DOCKER:  # type: ignore
    assert MIDDLEWARE[:1] == [  # type: ignore
        'django.middleware.security.SecurityMiddleware'
    ]
