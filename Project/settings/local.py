# This is the settings file that you use when you’re working on the project locally.
# Local development-specific settings include DEBUG mode, log level, and
# activation of developer tools like django-debug-toolbar.

# get_env_variable gets imported from base
from .main import *

USE_TZ = False

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_FILE_PATH = ''
# EMAIL_HOST =
# EMAIL_HOST_USER =
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# EMAIL_HOST_PASSWORD = get_env_variable('DEV_SECRET_3')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': get_env_variable('DEV_SECRET_2'),
        'HOST': 'localhost',
        'PORT': '5431',
    }
}

