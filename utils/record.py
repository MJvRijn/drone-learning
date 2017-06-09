from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

import os, cv2, rospy, random, string

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class Trajectory(object):
    _index = 0
    _id = 'AAAAA'
    _latest_image = None
    _actions = []
    _images = []

    def __init__(self, name, settings):
        self._name = name
        self._settings = settings
        self.subscribe_to_images()

    def record(self, action):
        self._actions.append(action)
        self._images.append(self._latest_image)
        self._index += 1

    def start_new(self):
        self._index = 0
        self._id = ''.join([random.choice(string.ascii_uppercase) for _ in range(5)])
        self._actions = []
        self._images = []

    def write(self):
        actions_path = '{}/{}/{}.txt'.format(self._settings.get_recordings_dir(), self._name, self._id)
        images_path = '{}/{}/{}/'.format(self._settings.get_recordings_dir(), self._name, self._id)

        # Create recording directories
        if not os.path.exists(images_path):
            os.makedirs(images_path)

        # Write actions
        with open(actions_path, 'w+') as actions_file:
            actions_file.write('\n'.join(self._actions))

        # Write images
        bridge = CvBridge()

        for i in range(len(self._images)):
            cv2_img = bridge.imgmsg_to_cv2(self._images[i], 'bgr8')
            cv2.imwrite('{}{}.jpg'.format(images_path, i), cv2_img)

        print(self._id)

    def read(self):
        # actions_path = '{}/{}/actions.txt'.format(self._settings.get_recordings_dir(), self._name)

        # with open(actions_path, 'r') as f:
        #     self._actions = f.read().split('\n')[:-1]
        #     self._index = 0

        print('Trajectory playback currently unavailable')

    def get_action():
        if self._index < len(self._actions):
            action = self.actions[self.index]
            self._index += 1
            return action
        else:
            return None

    def subscribe_to_images(self):
        rospy.Subscriber(self._settings.get_ros_camera_channel(), Image, self.image_callback, queue_size = 1)

    def image_callback(self, message):
        self._latest_image = message




