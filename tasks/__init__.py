# -*- coding: utf-8 -*-
import os
import sys

from celery import Celery

import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

argv = sys.argv

task_msg = Celery( \
        'tasks',
        include=[
            # 'celeries.fund_huitianfu',
        ])

if '--config=production' in argv:
    task_msg.config_from_object('tasks.conf.production')
else:
    task_msg.config_from_object('tasks.conf.local')

# global config
config = task_msg.conf

if __name__ == '__main__':
    task_msg.start()
