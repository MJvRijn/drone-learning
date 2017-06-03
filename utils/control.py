from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import atexit, select, os, cv2, rospy, random

import numpy as np

from subprocess import Popen, PIPE
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

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

class ModelController(object):
    _latest_image = None

    def __init__(self, settings):
        self._settings = settings
        self.subscribe_to_images()

    def get_action(self):
        if self._settings.get_model_name() == 'random':
            return self.random_model()

    def subscribe_to_images(self):
        rospy.Subscriber(self._settings.get_ros_camera_channel(), Image, self.image_callback, queue_size = 1)

    def image_callback(self, message):
        self._latest_image = message

    def random_model(self):
        image = np.asarray(self._latest_image)

        return ['HOVER', 'FORWARD', 'CLOCKWISE', 'ANTICLOCKWISE'][random.randint(0,3)]
