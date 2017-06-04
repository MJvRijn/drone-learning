from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse, rospy

from utils.settings import SettingsManager
from utils.helpers import Log
from utils.ros import Publisher
from utils.record import Trajectory
from utils.control import ModelController, KeyboardController

# Parse Arguments
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-r', '--record', type=str, metavar='NAME', help='record a trajectory')
group.add_argument('-p', '--play', type=str, metavar='NAME', help='play a recorded trajectory')
group.add_argument('-m', '--manual', action='store_true', help='control the drone manually')
group.add_argument('-i', '--interactive', action='store_true', help='get actions from server')
args = parser.parse_args()

record = play = manual = interactive = False
if args.record:
	record = True
if args.play:
	play = True
if args.manual:
	manual = True
if args.interactive:
	interactive = True

# Load settings and logger
settings = SettingsManager()
output = Log(settings)
publisher = Publisher(settings)

# Initialise controller and recording
if manual or record:
	controller = settings.get_manual_controller()

	if record:
		recording = Trajectory(args.record, settings)

elif play:
	controller = Trajectory(args.play, settings)
	controller.read()

elif interactive: 
	keyboard = KeyboardController(settings)
	controller = ModelController(settings, output)


# Control loop
rospy.init_node('control', anonymous=True)
rate = rospy.Rate(settings.get_rate())
airborne = False

while not rospy.is_shutdown():
	action = controller.get_action()

	# Override start and stop from keyboard
	if interactive:
		kba = keyboard.get_action()
		if kba == 'START' or kba == 'STOP':
			action = kba

	if action == None:
		output.logi('No more actions available')
		break

	elif action == 'START' and not airborne:	
		output.logi('Starting trajectory')
		airborne = True
		publisher.publish_start()
		
	elif action == 'STOP' and airborne:
		output.logi('Stopping trajectory')
		airborne = False
		publisher.publish_stop()

		# Finalise recprding
		if record: 
			recording.write()
			break

	elif airborne:
		if action == 'START': action = 'HOVER'

		output.logi('Performing action: ' + action)
		publisher.publish_move(action)

		if record:
			recording.record(action)

	# Sleep
	rate.sleep()
