#!/usr/bin/env python
import rospy
import serial
import checksum
from serial import SerialException
from std_msgs.msg import String
import create_dummy_msg as cdm

from sensor_msgs.msg import Imu
from sensor_msgs.msg import MagneticField as Mag
from inertialsense.msg import Rawgps
from inertialsense.msg import Bar


# code for using inertial sense library to convert binary data to ROS messages

def IS_raw2msg(ser):
    msgs = dict()
    msgcreator = cdm()
    #takes in the serial connection information
    bitstream = ser.read(ser.inWaiting())
    if len(bitstream) != 0:
        rospy.loginfo('Reading data from serial')
        ## here is where function calls to IS c++ lib are made to parse data.
        #for now creating dummy data
        msgs['GPS'] = msgcreator.dummy_gps();
        msgs['IMU'] = msgcreator.dummy_imu();
        msgs['MAG'] = msgcreator.dummy_mag();
        msgs['BAR'] = msgcreator.dummy_bar();
    
    return msgs
            
 
 


             