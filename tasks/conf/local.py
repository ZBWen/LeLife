# -*- coding: utf-8 -*-
from tasks.conf.base import *

DATABASES = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'leLife',
    'charset':'utf8'
}

BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

REDIS_URL = 'redis://127.0.0.1:6379/0'

CELERY_IMPORTS=('tasks.service.lottery')

from datetime import timedelta
from celery.schedules import crontab
# 定期执行任务
CELERYBEAT_SCHEDULE = {
	# 获得指定期号开奖号码
    'select-new-jbK8':{
        'task': 'tasks.service.lottery.NewPrevkeno',
        'schedule': crontab(minute='*/1'),
        "options":{},
        'args': ()
    },
}
