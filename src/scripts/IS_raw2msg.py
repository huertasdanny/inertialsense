#!/usr/bin/env python
import rospy
import serial
import checksum
from serial import SerialException
from std_msgs.msg import String
from create_dummy_msg import msg_creator

from sensor_msgs.msg import Imu
from sensor_msgs.msg import MagneticField as Mag
from inertialsense.msg import Rawgps
from inertialsense.msg import Bar


# code for using inertial sense library to convert binary data to ROS messages

def IS_raw2msg(ser):
    msgs = dict()
    
    msg2create = rospy.get_param('dataDesired')
    #takes in the serial connection information
    bitstream = ser.read(ser.inWaiting())
    if len(bitstream) != 0:
        rospy.loginfo('Reading data from serial')
        ## here is where function calls to IS c++ lib are made to parse data.
        #for now creating dummy data
        for topic, makemsg in msg2create.items():
            if makemsg:
                msgs[topic] = msg_creator(topic)
                rospy.loginfo('Received parsed %s message', topic)
                    
                
    else:
        rospy.loginfo('no data received')
    return msgs