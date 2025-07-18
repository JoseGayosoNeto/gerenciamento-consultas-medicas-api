import os

from .base import BASE_DIR

if not os.getenv('DEV_SECRET_KEY'):
    SECRET_KEY = 'django-insecure-c^4axmu@4n0ca*$a8fx3#a23$@8-!kg^o-l*@i7+vpbo%$eg9k'
else:
    os.getenv('DEV_SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

IN_DOCKER = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
