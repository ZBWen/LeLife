# -*- coding: utf-8 -*-
from tasks.conf.base import *

DATABASES = {
    'DBHOST': '',
    'DBPORT': 3306,
    'DBUSER': 'user_51visa',
    'DBPWD': '51ViSA51visa',
    'DBNAME': 'dj_51visa',
    'DBCHAR':'utf8',
    'MINCACHED':10,
    'MAXCACHED':200
}

BROKER_URL = 'redis://:6379/0'
CELERY_RESULT_BACKEND = 'redis://:6379/0'

REDIS_URL = 'redis://:6379/0'

from datetime import timedelta
from celery.schedules import crontab
# 定期执行任务
CELERYBEAT_SCHEDULE = {
}
