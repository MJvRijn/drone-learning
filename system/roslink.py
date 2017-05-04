#!/usr/bin/env python

import rospy
from ds4 import ds4
from std_msgs.msg import Empty, String
from geometry_msgs.msg import Twist, Vector3

def control():
    rospy.init_node('control', anonymous=True)
    rate = rospy.Rate(10)

    takeoff_channel = rospy.Publisher('ardrone/takeoff', Empty, queue_size=10)
    land_channel = rospy.Publisher('ardrone/land', Empty, queue_size=10)
    reset_channel = rospy.Publisher('ardrone/reset', Empty, queue_size=10)
    movement_channel = rospy.Publisher('cmd_vel', Twist, queue_size=10)


    controller = ds4()

    while not rospy.is_shutdown():
        action = controller.get_action()
        print(action)

        if action == 'HOVER':
            command = Twist(Vector3(0.0,0.0,0.0), Vector3(0.0,0.0,0.0))
            movement_channel.publish(command)
        if action == 'RESET':
            reset_channel.publish(Empty())
        elif action == 'TAKEOFF':
            takeoff_channel.publish(Empty())
        elif action == 'LAND':
            land_channel.publish(Empty())
        elif action == 'UP':
            command = Twist(Vector3(0.0,0.0,1.0), Vector3(0.0,0.0,0.0))
            movement_channel.publish(command)
        elif action == 'DOWN':
            command = Twist(Vector3(0.0,0.0,-1.0), Vector3(0.0,0.0,0.0))
            movement_channel.publish(command)

        rate.sleep()

if __name__ == '__main__':
   try:
       control()
   except rospy.ROSInterruptException:
       pass
