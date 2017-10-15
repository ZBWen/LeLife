# -*- coding: utf-8 -*-
import requests

from tasks.utils.redis import redis_connt

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

def open_url(url,data=None,headers=headers,
            proxies={}, POST=False, use_proxies=False, timeout=15):
    proxie_list = [None]
    if use_proxies:
        proxie_list = redis_connt.lrange('PROXIES_IP', 0, -1)
    for proxie in proxie_list:
        print ('proxie')
        if proxie:
            proxies = {
                "http": u'http://{}'.format(proxie),
                "https": u'https://{}'.format(proxie),
                }
        try:
            print ('try')
            if not POST:
                req = requests.get(url,headers=headers,proxies=proxies,timeout=timeout)
            else:
                req = requests.post(url,data=data,headers=headers,proxies=proxies,timeout=timeout)
            print (req)
            if req.status_code == 200:
                html = req.content
            else:
                raise Exception('status_code error:{}'.format(req.status_code))
        except requests.exceptions.ConnectTimeout:
            redis_connt.lrem('PROXIES_IP',proxie,0)
            continue
        except requests.exceptions.ConnectionError:
            redis_connt.lrem('PROXIES_IP',proxie,0)
            continue
        except Exception as e:
            if proxie:
                continue
            else:
                raise Exception(e)
        break
    return html