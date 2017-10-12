# This is the settings file used by your live production server(s). That is, the
# server(s) that host the real live website. This file contains production-level
# settings only.

# Make sure no datetime objects are naive!!!
USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST =
# EMAIL_HOST_USER = 'gideon@walkerteksolutions.com'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# EMAIL_HOST_PASSWORD =
# EMAIL_PORT =
# EMAIL_USE_TLS =