from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import paramiko, string, random, time, cv2, os

import numpy as np

from .helpers import Log

class ServerManager(object):

    def __init__(self, settings, log):
        self._settings = settings
        self._log = log
        self._ssh = self.connect()

    def train_model(self, model_name):
        pass

    def classify_image(self, image):
        # Transfer File
        filename = self.transfer_image(image)

        # Wait for classification result
        
        # _, stdout, stderr = self._ssh.exec_command('source ~/imitation/bin/activate; python drone/classify.py {}'.format(filename))
        
        # for line in stderr.readlines():
        #     print(line)

        # return stdout.readlines()[0].strip('\n')
        return 'HOVER'

    def transfer_image(self, image):
        filename = ''.join([random.choice(string.ascii_uppercase) for _ in range(20)])
        local_file = '/tmp/{}.jpg'.format(filename)
        remote_file = '/home/{}/drone/classify/{}.jpg'.format(self._settings.get_server_details()[1], filename)

        cv2.imwrite(local_file, image)
        sftp = self._ssh.open_sftp()

        sftp.put(local_file, remote_file)

        os.remove(local_file)

        return filename

    def connect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        addr, user, passw = self._settings.get_server_details()

        ssh.connect(addr, username = user, password = passw)

        self._log.logi('Connected to remote server')

        return ssh