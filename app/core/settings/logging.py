import os
from typing import Dict

LOG_LEVEL = os.getenv('BASE_LOG_LEVEL', 'DEBUG')

LOGGING: Dict = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s',
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
            'filename': 'app/logs/app.log',
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
