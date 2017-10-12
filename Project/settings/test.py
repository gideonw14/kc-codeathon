# Settings for running tests including test runners, in-memory database
# definitions, and log settings.
from .main import *

USE_TZ = False

DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, '/Project/static/main/temp')

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