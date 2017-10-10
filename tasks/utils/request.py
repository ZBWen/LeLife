# -*- coding: utf-8 -*-
import requests

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

def open_url(url,data=None,headers=headers,POST=False, timeout=15):
    proxies = {
        "http": "http://180.168.179.193:8080",
        "https": "http://180.168.179.193:8080",
        }
    if not POST:
        req = requests.get(url,headers=headers,proxies=proxies,timeout=timeout)
    else:
        req = requests.post(url,data=data,headers=headers,proxies=proxies,timeout=timeout)
    if req.status_code == 200:
        html = req.content
    else:
        print (url)
        print (req.status_code)
    return html