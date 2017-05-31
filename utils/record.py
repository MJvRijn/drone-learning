import os, cv2, rospy

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class Trajectory(object):
    _index = 0
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

    def write(self):
        actions_path = '{}/{}/actions.txt'.format(self._settings.get_recordings_dir(), self._name)
        images_path = '{}/{}/images/'.format(self._settings.get_recordings_dir(), self._name)

        # Create recording directories
        if not os.path.exists(images_path):
            os.makedirs(images_path)

        # Write actions
        with open(actions_path, 'w+') as actions_file:
            actions_file.write('\n'.join(self._actions))

        # Write images
        bridge = CvBridge()

        for image in self._images:
            print(image)
            # cv2_img = bridge.imgmsg_to_cv2(image, 'bgr8')
            # cv2.imwrite('{}{}.jpg'.format(images_path, self._index), cv2_img)

    def read(self):
        actions_path = '{}/{}/actions.txt'.format(self._settings.get_recordings_dir(), self._name)

        with open(actions_path, 'r') as f:
            self._actions = f.read().split('\n')[:-1]
            self._index = 0

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




