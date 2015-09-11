from __future__ import absolute_import

import dj_database_url

from .base import *

DEBUG = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['clone-instagram.herokuapp.com']

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
