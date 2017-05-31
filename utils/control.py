from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import atexit, select

from subprocess import Popen, PIPE

class KeyboardController(object):

    def __init__(self, settings):
        self._settings = settings
        self._last_action = 'HOVER'
        self._listener = Popen(['python', '-u', 'scripts/keyboard.py'], stdout=PIPE)

        self._poll = select.poll()
        self._poll.register(self._listener.stdout, select.POLLIN)

        atexit.register(self._listener.terminate)

    def get_action(self):
        # Read stdout of listener
        if self._poll.poll(1):
            self._last_action = self._listener.stdout.readline().decode('utf-8').strip('\n')

        return self._last_action