from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import paramiko

from .helpers import Log

class ServerManager(object):

    def __init__(self, settings, log):
        self._settings = settings
        self._log = log
        self._ssh = self.connect()

    def train_model(self, model_name):
        pass

    def classify_image(self, image):
        return 'HOVER'

    def connect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        addr, user, passw = self._settings.get_server_details()

        ssh = ssh.connect(addr, username = user, password = passw)

        self._log.logi('Connected to remote server')

        return ssh