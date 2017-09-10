# -*- coding: utf-8 -*-
from pyquery import PyQuery

from tasks.utils.request import open_url

# 根据url获取快乐8数据
def get_prevkeno_list(url):
    html = open_url(url)
    py = PyQuery(html)
    table = py('.lott_cont')('table')
    trs = table('tr')
    trs.pop(0)
    for tr in trs.items():
        tds = tr('td')
        print (tds[0].text)

# 获得指定期号开奖号码
def get_prevkeno(url):
    issue = None
    lottery = None
    frisbee = None
    date = None
    html = open_url(url)
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