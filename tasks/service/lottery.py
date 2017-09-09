# -*- coding: utf-8 -*-
import time

from tasks import config
from tasks import task_msg
from tasks.service.prevkeno import *
from tasks.utils.redis import redis_connt


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
