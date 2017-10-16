# -*- coding: utf-8 -*-
import time
import datetime

from tasks import config
from tasks import task_msg
from tasks.service.keno import *
from tasks.service.miss import *
from tasks.utils.redis import redis_connt

class NewPrevkeno(task_msg.Task):
    max_retries = 0
    default_retry_delay = 0

    def run(self, *args, **kwargs):
        issue = None
        NUM = redis_connt.get('NEW_PREVKENO',default=850555)
        if NUM:
            count = 0
            while True:
                count += 1
                if count > 20:
                    break
                print (NUM)
                try:
                    URL = 'http://www.bwlc.net/bulletin/keno.html?num={}'.format(NUM)
                    issue, lottery, frisbee, date = get_prevkeno(URL)
                    if issue:
                        break
                    time.sleep(1)
                    URL = 'http://www.bwlc.net/bulletin/prevkeno.html?num={}'.format(NUM)
                    issue, lottery, frisbee, date = get_prevkeno(URL)
                    if issue:
                        break
                    time.sleep(1)
                    URL = 'http://www.bwlc.net/bulletin/keno.html'
                    issue, lottery, frisbee, date = get_prevkeno(URL)
                    if issue and str(NUM) == str(issue):
                        break
                    time.sleep(1)
                    URL = 'http://www.bwlc.net/bulletin/prevkeno.html'
                    issue, lottery, frisbee, date = get_prevkeno(URL)
                    if issue and str(NUM) == str(issue):
                        break
                except Exception as e:
                    print (u'%s' % e)
            print (issue, lottery, frisbee, date)
            nums = pc28_num(lottery.split(','))
            if str(NUM) == str(issue):
                set_keno(
                    issue=issue,
                    lottery=lottery,
                    frisbee=frisbee,
                    date=date,
                    pc_nums=nums,
                    pc_sum=sum(nums))
                print (int(issue)+1)
            # 更新 新的待获取期号
            redis_connt.set('NEW_PREVKENO',int(issue)+1)
            redis_connt.expire('NEW_PREVKENO', 3600*24*7)

class PrevkenoMiss(task_msg.Task):
    max_retries = 0
    default_retry_delay = 0

    def run(self, *args, **kwargs):
        try:
            prevkeno = Prevkeno()
            prevkeno.select_miss()
        except Exception as e:
            print (u'%s' % e)

class Test(task_msg.Task):
    max_retries = 0
    default_retry_delay = 0

    def run(self, *args, **kwargs):
        PAGE = int(redis_connt.get('PREVKENO_PAGE',default=15007))
        while PAGE:
            print (PAGE)
            try:
                last_keno = int(redis_connt.get('LAST_KENO',default=0))
                URL = 'http://www.bwlc.net/bulletin/prevkeno.html?page={}'.format(PAGE)
                data_list = get_prevkeno_list(URL)
                if data_list:
                    set_page = redis_connt.get('PREVKENO_PAGE',default=15007)
                    if int(set_page) == PAGE:
                        for data in data_list:
                            issue = data['issue']
                            lottery = data['lottery']
                            assert issue
                            if int(issue) == last_keno:
                                redis_connt.set('PREVKENO_PAGE',0)
                                break
                            nums = pc28_num(lottery.split(','))
                            set_keno(pc_nums=nums,pc_sum=sum(nums),**data)
                        PAGE -=1
                        redis_connt.set('PREVKENO_PAGE',PAGE)
            except Exception as e:
                print (URL)
                print (u'%s' % e)
