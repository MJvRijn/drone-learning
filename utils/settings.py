from .errors import SettingsException
from .control import KeyboardController

class SettingsManager(object):

    # ROS settings
    _ros_rate = 10
    _ros_takeoff_channel = 'ardrone/takeoff'
    _ros_land_channel = 'ardrone/land'
    _ros_movement_channel = 'cmd_vel'
    _ros_camera_channel = 'ardrone/front/image_raw'

    # Directory settings
    _dir_recordings = 'recordings'
    _dir_training_sets = 'training'
    _dir_models = 'models'

    # Control settings
    _controller = 'keyboard'

    # Server settings
    _server_address = '127.0.0.1'
    _server_api = '/image'

    # Action space
    _actions = {'HOVER':            ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0]),
                'ANTICLOCKWISE':    ([0.0, 0.0, 0.0], [0.0, 0.0, 1.0]),
                'CLOCKWISE':        ([0.0, 0.0, 0.0], [0.0, 0.0,-1.0]),
                'FORWARD':          ([1.0, 0.0, 0.0], [0.0, 0.0, 0.0])}


    def __init__(self):
        self.read()

    def read(self):
        pass

    def get_manual_controller(self):
        if self._controller == 'keyboard':
            return KeyboardController(self)
        else:
            raise SettingsException('controller type must be keyboard')

    def get_rate(self):
        if self._ros_rate in range(1, 60):
            return self._ros_rate
        else:
            raise SettingsException('rate must be between 1 and 60hz')

    def get_ros_movement_channels(self):
        return self._ros_takeoff_channel, \
               self._ros_land_channel, \
               self._ros_movement_channel

    def get_actions(self):
        return self._actions