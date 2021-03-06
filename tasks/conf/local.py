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
    # # 刷新代理http
    # 'ref_ip':{
    #     'task': 'tasks.utils.proxies.RefreshProxies',
    #     'schedule': crontab(
    #         minute='0,5,10,15,20,25,30,35,40,45,50,55'),
    #     "options":{},
    #     'args': ()
    # },

    # # 北京快乐8 遗漏
    # 'ref_ip':{
    #     'task': 'tasks.service.lottery.PrevkenoMiss',
    #     'schedule': crontab(minute='*/1'),
    #     "options":{},
    #     'args': ()
    # },
	# 获得指定期号开奖号码
    'setMissPrevkeno':{
        'task': 'tasks.service.lottery.SetMissPrevkeno',
        'schedule': crontab(
            hour='22',
            minute='3'),
        # crontab(
        #     hour='9,10,11,12,13,14,15,16,17,18,19,20,21,22,23',
        #     minute='0,5,10,15,20,25,30,35,40,45,50,55'),
        # "options":{'queue':'tasks'},
        'args': ()
    },
    # # 获得所有历史记录
    # 'select-history-jbK8':{
    #     'task': 'tasks.service.lottery.Test',
    #     'schedule': crontab(hour=21,minute=33),
    #     "options":{},
    #     'args': ()
    # },
}
