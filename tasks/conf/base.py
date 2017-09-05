# -*- coding: utf-8 -*-
CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_TRACK_STARTED = True
CELERY_DISABLE_RATE_LIMITS = True

# CELERY_IGNORE_RESULT = True

# CELERY_ANNOTATIONS = {
#     'tasks.divide': {'rate_limit': '1/s'}
# }

#任务结果的时效时间
CELERY_TASK_RESULT_EXPIRES = 3600*24*7

# CELERY_DEFAULT_QUEUE = "celery" # 默认的队列，如果一个消息不符合其他的队列就会放在默认队列里面
