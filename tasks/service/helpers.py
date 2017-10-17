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
		if self.now.hour == 9:
			if self.now.minute < 5:
				return True
		return False
