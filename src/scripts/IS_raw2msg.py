#!/usr/bin/env python
import rospy
import serial
import sys
sys.path.append(r'/home/catkin_ws/src/inertialsense/src/scripts')
import checksum
from serial import SerialException
from std_msgs.msg import String
from sensor_msgs.msg import Imu


# code for using inertial sense library to convert binary data to ROS messages