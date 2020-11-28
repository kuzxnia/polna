from .base import *

import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xjr(rur+l6*&^pa(io-&url&(n&m25$#%-psr4uc8_i#1x9x_*'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
