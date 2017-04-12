#!/usr/bin/env python
import rospy
import IS_raw2msg
import serial
import sys
sys.path.append(r'/home/catkin_ws/src/inertialsense/src/scripts')

from init_pub_sub import initpubs

def initnode():
    rospy.init_node('listener', anonymous=True)