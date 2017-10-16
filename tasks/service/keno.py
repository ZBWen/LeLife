# -*- coding: utf-8 -*-
import time
import requests
import datetime
from pyquery import PyQuery

from tasks.utils.request import Request
from tasks.utils.redis import redis_connt
from tasks.utils.mysql import Mysql

# 根据url获取快乐8数据
def get_prevkeno_list(url):
    keno_list = []
    html = Request().open_url(url,timeout=15)
    py = PyQuery(html)
    table = py('.lott_cont')('table')
    trs = table('tr')
    trs.pop(0)
    for tr in trs.items():
        tds = tr('td')
        issue = tds[0].text
        lottery = tds[1].text
        frisbee = tds[2].text
        date = tds[3].text
        keno_list.append({
            "issue":issue,
            "lottery":lottery,
            "frisbee":frisbee,
            "date":date,
            })
    return keno_list

# 获得指定期号开奖号码
def get_prevkeno(url):
    issue = None
    lottery = None
    frisbee = None
    date = None
    html = Request().open_url(url,timeout=15)
    print (url)
    py = PyQuery(html)
    table = py('.lott_cont')('table')
    trs = table('tr')
    trs.pop(0)
    for tr in trs.items():
        tds = tr('td')
        issue = tds[0].text
        lottery = tds[1].text
        frisbee = tds[2].text
        date = tds[3].text
    return issue, lottery, frisbee, date

# pc28 num
def pc28_num(nums):
    nums = [int(num) for num in nums]
    nums.sort()
    _a = int(str(sum(nums[0:6]))[-1])
    _b = int(str(sum(nums[6:12]))[-1])
    _c = int(str(sum(nums[12:18]))[-1])
    return _a,_b, _c

def set_keno(**kwargs):
    issue = kwargs['issue']
    lottery = kwargs['lottery']
    frisbee = kwargs['frisbee']
    date = kwargs['date']
    pc_nums = kwargs['pc_nums']
    pc_sum = kwargs['pc_sum']
    # 元祖转字符串
    pc_nums = ','.join([str(num) for num in pc_nums])
    # 数据保存到redis
    KENO_KEY = 'KENO-{}'.format(issue)
    redis_connt.hset(KENO_KEY,'issue',issue)
    redis_connt.hset(KENO_KEY,'lottery',lottery)
    redis_connt.hset(KENO_KEY,'frisbee',frisbee)
    redis_connt.hset(KENO_KEY,'date',date)
    redis_connt.hset(KENO_KEY,'pc_nums',pc_nums)
    redis_connt.hset(KENO_KEY,'pc_sum',pc_sum)
    redis_connt.expire(KENO_KEY, 3600*24*360)

    mysql = Mysql()
    SQL = "INSERT INTO lottery_bjkeno (issue,nums,frisbee,pc_nums,pc_sum,date,create_date,update_date) VALUES ('{}','{}','{}','{}','{}','{}','{}');" \
        .format(issue,lottery,frisbee,pc_nums,pc_sum,date,datetime.datetime.now(),datetime.datetime.now())
    try:
        mysql.insertOne(SQL)
        mysql.dispose()
    except Exception as e:
        print ('e %s' % e)
        mysql.dispose(isEnd=0)
