# -*- coding: utf-8 -*-
import requests

from tasks.utils.redis import redis_connt

class Request(object):
    proxies = {}
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Accept-Language': 'en-us;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        }
    timeout = 30

    def __inif__(self):
        self.proxie_list = redis_connt.lrange('PROXIES_IP', 0, -1)


    def get(self,url,headers=headers,proxies=proxies,timeout=30):
        req = requests.get(url,headers=headers,proxies=proxies,timeout=timeout)
        return req

    def post(self,url,data,headers=headers,proxies=proxies,timeout=30):
        req = requests.post(url,data=data,headers=headers,proxies=proxies,timeout=timeout)
        return req

    def open_url(url,data=None,headers=headers,
                        proxies={}, POST=False, use_proxies=False, timeout=15):
        kwargs = {
            "headers":headers,
            "proxies":proxies,
            "timeout":timeout
        }
        if use_proxies:
            for proxie in self.proxie_list:
                proxies = {
                    "http": u'http://{}'.format(proxie),
                    "https": u'https://{}'.format(proxie),
                    }
                try:
                    if not POST:
                        req = self.get(url,**kwargs)
                    else:
                        req = self.post(url,data=data,**kwargs)
                except requests.exceptions.ConnectTimeout:
                    redis_connt.lrem('PROXIES_IP',proxie,0)
                    continue
                except requests.exceptions.ConnectionError:
                    redis_connt.lrem('PROXIES_IP',proxie,0)
                    continue
                except Exception as e:
                    continue
                break
        else:
            if not POST:
                req = self.get(url,**kwargs)
            else:
                req  = self.post(url,data=data,**kwargs)
        return req.content