# -*- coding: utf-8 -*-
from tasks.conf.base import *

DATABASES = {
    'DBHOST': '127.0.0.1',
    'DBPORT': 3306,
    'DBUSER': 'root',
    'DBPWD': 'root',
    'DBNAME': 'leLife',
    'DBCHAR':'utf8',
    'MINCACHED':10,
    'MAXCACHED':200
}

BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

REDIS_URL = 'redis://127.0.0.1:6379/0'

CELERY_IMPORTS=('tasks.service.lottery')

from datetime import timedelta
from celery.schedules import crontab
# 定期执行任务
CELERYBEAT_SCHEDULE = {
	# 获取新加坡机构列表
    'select-new-jbK8':{
        'task': 'tasks.service.lottery.Test',
        'schedule': crontab(minute='*/1'),
        "options":{},
        'args': ()
    },
}
