from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import time

class Log(object):

	def __init__(self, settings):
		self._start_time = time.time()
		self._settings = settings

	def logi(self, message):
		print('[{:0.2f} INFO] {}'.format(time.time() - self._start_time, message))
