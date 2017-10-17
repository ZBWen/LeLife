# -*- coding: utf-8 -*-
import time
import datetime

class IsRunTime(object):

    def __init__(self, _str):
        self._str = _str
        self.now = datetime.datetime.now()

    def verify(self):
        if self._str == 'NewPrevkeno':
            self.prevkeno()

    def prevkeno(self):
        if self.now.hour < 9:
            return False
        if self.now.hour == 9 and self.now.minute < 5:
            return False
        return True
