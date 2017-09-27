# -*- coding: utf-8 -*-
import os
from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'leLife',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '',
        'OPTIONS': {'charset':'utf8mb4'},
        'CONN_MAX_AGE': 600,
    }
}

# CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': '54ac2433ff9b465e.m.cnhzaliqshpub001.ocs.aliyuncs.com:11211',
#        'TIMEOUT': 3600*48,
#        'KEY_PREFIX': 'leLife_'
#    }
# }

# REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = ('rest_framework.renderers.JSONRenderer',)