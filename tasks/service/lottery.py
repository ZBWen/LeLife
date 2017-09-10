# -*- coding: utf-8 -*-
import time
import datetime

from tasks import config
from tasks import task_msg
from tasks.service.prevkeno import *
from tasks.utils.redis import redis_connt

class NewPrevekno(task_msg.Task):
    max_retries = 3
    default_retry_delay = 1000*15

    def run(self, *args, **kwargs):
        issue = None
        NUM = redis_connt.get('NEW_PREVKENO')
        if NUM:
            URL = 'http://www.bwlc.net/bulletin/keno.html?num={}'.format(NUM.decode('utf-8'))
            issue, lottery, frisbee, date = get_prevkeno(URL)
            if not issue:
                time.sleep(5)
                URL = 'http://www.bwlc.net/bulletin/prevkeno.html?num={}'.format(NUM.decode('utf-8'))
                issue, lottery, frisbee, date = get_prevkeno(URL)
        try:
            assert issue
            nums = pc28_num(lottery.split(','))
            print (issue, lottery, frisbee, date, nums, sum(nums))
            redis_connt.set('NEW_PREVKENO',int(issue)+1)
            redis_connt.expire('NEW_PREVKENO', 3600*24*7)
        except Exception as exc:
            raise self.retry(exc=exc, countdown=10)

class Test(task_msg.Task):
    max_retries = 0
    default_retry_delay = 0

    def run(self, *args, **kwargs):
        PAGE = redis_connt.get('PREVKENO_PAGE',default=14816)
        while PAGE:
            URL = 'http://www.bwlc.net/bulletin/prevkeno.html?page={}'.format(PAGE)
            get_prevkeno_list(URL)
            PAGE -=1
            redis_connt.set('PREVKENO_PAGE',PAGE)
