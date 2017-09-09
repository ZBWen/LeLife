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