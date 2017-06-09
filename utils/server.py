from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import paramiko, string, random, time, cv2, os, tarfile

import numpy as np

from .helpers import Log

class ServerManager(object):

    def __init__(self, settings, log):
        self._settings = settings
        self._log = log
        self._ssh = self.connect()

    def train_model(self, model_name, dataset):
        directory = '{}/{}'.format(self._settings.get_recordings_directory(), dataset)
        archive = '{}.tar.gz'.format(directory)

        with tarfile.open(archive, 'w:gz') as tar:
            tar.add(directory, arcname=os.path.basename(directory))
        
        # Transfer file
        sftp = self._ssh.open_sftp()
        remote_file = '/home/{}/drone/train/{}.tar.gz'.format(self._settings.get_server_details()[1], dataset)

        sftp.put(archive, remote_file)

        # Wait for file to arrive

        # Start training

        # Wait for training to complete

    def classify_image(self, image):
        # Transfer File
        filename = self.transfer_image(image)

        # Wait for classification result
        while True:
            _, stdout, stderr = self._ssh.exec_command('cat ~/drone/classify/{}.txt'.format(filename))

            result = stdout.readlines()

            print(result)

            if result:
                return result[0]

            time.sleep(0.05)

    def classify_image(self, image):
        filename = ''.join([random.choice(string.ascii_uppercase) for _ in range(20)])
        local_file = '/tmp/{}.jpg'.format(filename)
        remote_file = '/home/{}/drone/classify/{}.jpg'.format(self._settings.get_server_details()[1], filename)

        cv2.imwrite(local_file, image)

        # Transfer file
        sftp = self._ssh.open_sftp()

        while True:
            try:
                sftp.put(local_file, remote_file)
            except IOError:
                time.sleep(0.01)
            else:
                break

        # Wait for classification
        while True:
            try:
                sftp.stat(remote_file.split('.')[0] + '.txt')
            except IOError:
                time.sleep(0.02)
            else:
                _, stdout, stderr = self._ssh.exec_command('cat ~/drone/classify/{}.txt'.format(filename))

                result = stdout.readlines()
                action = result[0]
                break

        os.remove(local_file)

        return action

    def connect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        addr, user, passw = self._settings.get_server_details()

        ssh.connect(addr, username = user, password = passw)

        self._log.logi('Connected to remote server')

        return ssh