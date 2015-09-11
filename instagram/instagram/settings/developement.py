from __future__ import absolute_import

from .base import *

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += (
    'debug_toolbar',
)

STATICFILES_DIRS = [os.path.join(BASE_DIR, '..', 'static'), ]
