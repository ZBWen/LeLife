# -*- coding: utf-8 -*-
import time
import datetime

from tasks.service.keno import *

class IsRunTime(object):

    def __init__(self, _str):
        self._str = _str
        self.now = datetime.datetime.now()

    def verify(self):
        if self._str == 'NewPrevkeno':
            return self.prevkeno()

    def prevkeno(self):
        if self.now.hour < 9:
            return False
        if self.now.hour == 9 and self.now.minute < 5:
            return False
        return True

def get_prevkeno_num(NUM):
    time.sleep(3)
    URL = 'http://www.bwlc.net/bulletin/prevkeno.html?num={}'.format(NUM)
    issue, lottery, frisbee, date = get_prevkeno(URL)
    return issue, lottery, frisbee, date

def select_prevkeno(NUM):
    URL = 'http://www.bwlc.net/bulletin/keno.html?num={}'.format(NUM)
    issue, lottery, frisbee, date = get_prevkeno(URL)
    if issue:
        return issue, lottery, frisbee, date
    time.sleep(1)
    URL = 'http://www.bwlc.net/bulletin/prevkeno.html?num={}'.format(NUM)
    issue, lottery, frisbee, date = get_prevkeno(URL)
    if issue:
        return issue, lottery, frisbee, date
    time.sleep(1)
    URL = 'http://www.bwlc.net/bulletin/keno.html'
    issue, lottery, frisbee, date = get_prevkeno(URL)
    if issue and str(NUM) == str(issue):
        return issue, lottery, frisbee, date
    time.sleep(1)
    URL = 'http://www.bwlc.net/bulletin/prevkeno.html'
    issue, lottery, frisbee, date = get_prevkeno(URL)
    if issue and str(NUM) == str(issue):
        return issue, lottery, frisbee, date

    return None, None, None, None
