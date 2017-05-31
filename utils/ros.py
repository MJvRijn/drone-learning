from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import rospy

from std_msgs.msg import Empty, String
from geometry_msgs.msg import Twist, Vector3

class Publisher(object):

    def __init__(self, settings):
        self._settings = settings
        self._actions = settings.get_actions()

        start_channel, stop_channel, move_channel = self._settings.get_ros_movement_channels()
        self._start_publisher = rospy.Publisher(start_channel, Empty, queue_size=10)
        self._stop_publisher = rospy.Publisher(stop_channel, Empty, queue_size=10)
        self._move_publisher = rospy.Publisher(move_channel, Twist, queue_size=10)

    def publish_start(self):
        self._start_publisher.publish(Empty())

    def publish_stop(self):
        self._stop_publisher.publish(Empty())

    def publish_move(self, action):
        v = self._actions[action]
        message = Twist(Vector3(v[0][0], v[0][1], v[0][2]), Vector3(v[1][0], v[1][1], v[1][2]))
        self._move_publisher.publish(message)
