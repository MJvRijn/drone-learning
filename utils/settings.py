from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from .errors import SettingsException
from .control import KeyboardController

import os, shutil, json

class SettingsManager(object):

    # ROS settings
    _ros_rate = 10
    _ros_takeoff_channel = 'ardrone/takeoff'
    _ros_land_channel = 'ardrone/land'
    _ros_movement_channel = 'cmd_vel'
    _ros_camera_channel = 'ardrone/front/image_raw'

    # Directory settings
    _dir_recordings = 'recordings'
    _dir_remote_training_sets = 'train'
    _dir_remote_classification = 'classify'

    # Control settings
    _controller = 'keyboard'

    # Server settings
    _server_address = '127.0.0.1'
    _server_username = 'bob'
    _server_password = 'bob'

    # Action space
    _actions = {'HOVER':            ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0]),
                'ANTICLOCKWISE':    ([0.0, 0.0, 0.0], [0.0, 0.0, 1.0]),
                'CLOCKWISE':        ([0.0, 0.0, 0.0], [0.0, 0.0,-1.0]),
                'FORWARD':          ([1.0, 0.0, 0.0], [0.0, 0.0, 0.0])}

    # Model settings
    _model_name = 'remote'
    _model_remote_name = 'ff' # ff, cnn


    def __init__(self):
        self.read()

    def read(self):
        if not os.path.isfile('settings.json'):
            shutil.copyfile('settings.example.json', 'settings.json')

        with open('settings.json') as data:
            s = json.load(data)

            self._server_address = s['server_address']
            self._server_username = s['server_username']
            self._server_password = s['server_password']

    def get_server_details(self):
        return self._server_address, self._server_username, self._server_password

    def get_manual_controller(self):
        if self._controller == 'keyboard':
            return KeyboardController(self)
        else:
            raise SettingsException('controller type must be keyboard')

    def get_recordings_directory(self):
        return self._dir_recordings

    def get_rate(self):
        if self._ros_rate in range(1, 61):
            return self._ros_rate
        else:
            raise SettingsException('rate must be between 1 and 60hz')

    def get_ros_movement_channels(self):
        return self._ros_takeoff_channel, \
               self._ros_land_channel, \
               self._ros_movement_channel

    def get_ros_camera_channel(self):
        return self._ros_camera_channel

    def get_actions(self):
        return self._actions

    def get_recordings_dir(self):
        return self._dir_recordings

    def get_model_name(self):
        return self._model_name