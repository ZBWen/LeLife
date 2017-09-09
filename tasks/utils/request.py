# -*- coding: utf-8 -*-
import requests

def open_url(url,data=None,POST=True):
    if not POST:
        req = requests.get(url,timelout=15)
    else:
        req = requests.post(url,data=data,timeout=15)
    if req.status_code == 200:
        html = req.content
    return html