import os
from typing import Dict

from app.core.settings.environments.base import BASE_DIR

LOG_LEVEL = os.getenv('BASE_LOG_LEVEL', 'DEBUG')
LOG_FILE_PATH = os.getenv('LOG_FILE_PATH')
if not LOG_FILE_PATH:
    raise ValueError("Variável de ambiente LOG_FILE_PATH precisa ser definida.")

os.makedirs(os.path.dirname(os.path.join(BASE_DIR, LOG_FILE_PATH)), exist_ok=True)

LOGGING: Dict = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'filters': [],
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, LOG_FILE_PATH),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 7,
            'formatter': 'standard',
        },
    },
    'loggers': {
        logger_name: {
            'level': LOG_LEVEL,
            'propagate': True,
        } for logger_name in
        ('django', 'django.requests', 'django.db.backends', 'django.templates', 'app')
    },
    'root': {
        'level': LOG_LEVEL,
        'handlers': [
            'console',
            'file',
        ],
    },
}
