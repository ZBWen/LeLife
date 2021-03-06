# -*- coding: utf-8 -*-
import time
import datetime

from pyquery import PyQuery

from tasks import config
from tasks import task_msg
from tasks.utils.request import Request
from tasks.utils.redis import redis_connt

class RefreshProxies(task_msg.Task):
    max_retries = 0
    default_retry_delay = 0

    def run(self, *args, **kwargs):
        ip_list = []
        try:
            html = Request().open_url('http://www.xicidaili.com/nn/')
            pq = PyQuery(html)
            trs = pq('#ip_list')('tr')
            trs.pop() # remove first
            for tr in trs.items():
                speed = tr('.bar').eq(0).attr('title')
                if speed and speed[0] == '0':
                    tds = tr('td')
                    ip = '{}:{}'.format(tds.eq(1).text(),tds.eq(2).text())
                    ip_list.append(ip)
        except Exception as e:
            print (e)

        try:
            html = Request().open_url('http://www.goubanjia.com/free/gngn/index1.shtml')
            pq = PyQuery(html)
            trs = pq('#list')('.table')('tbody')('tr')
            for tr in trs.items():
                td_ip = tr.eq(0)('td').eq(0)
                ip = td_ip.remove('p').text().replace(' ','')
                ip_list.append(ip)
        except Exception as e:
            print (e)

        try:
            html = Request().open_url('http://www.kuaidaili.com/free/intr/1/')
            pq = PyQuery(html)
            trs = pq('#list')('.table')('tbody')('tr')
            for tr in trs.items():
                tds = tr('td')
                ip = '{}:{}'.format(tds.eq(0).text(),tds.eq(1).text())
                ip_list.append(ip)
                print (ip)
        except Exception as e:
            print (e)

        redis_connt.delete('PROXIES_IP')
        for ip in ip_list:
            redis_connt.lpush('PROXIES_IP',ip)