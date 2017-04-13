#!/usr/bin/env python

import rospy
from IS_raw2msg import IS_raw2msg
import serial
import sys
sys.path.append(r'/home/catkin_ws/src/inertialsense/src/scripts')
from serial import SerialException
from init_pub_sub import initpubs
#from IS_msgcallback import msgcallback

def openPort(port_settings):
    # print(port_settings)
    ser = serial.Serial(timeout=port_settings['tout'])
    possports = port_settings['pname']
    ser.baudrate = port_settings['baud']
    # iterate through possible ports trying to connect
    for port in possports:
        ser.port = port
        try:
            ser.close()
            ser.open()
            rospy.loginfo('Connected to port %s',port)
            return 1, ser
        except SerialException:
            rospy.loginfo('Could not connect to port %s', port)
    return 0, ser


def get_pub_data(ser, pubs):
    
    #rospy.loginfo('getting data from sensor')
    msgs = IS_raw2msg(ser)
    # # have msgs be dictionary of messages 
    # # possible for there to be less messages than publishers but not other way around
    if len(msgs) > len(pubs):
        rospy.logerr('Too many messages')
    else:
        for msg in msgs.keys():
            rospy.loginfo('Trying to publish %s data', msg)
            
            try:
                #msgcallback(msg)(msgs[msg])#if you want to know the data, calls a rospy.loginfo callback
                pubs[msg].publish(msgs[msg])
                rospy.loginfo('Published %s data',msg)
            except rospy.ROSException:
                rospy.logerr('Could not publish %s data', msg)
    
if __name__ == '__main__':    
    rospy.init_node('IS_dataparser', anonymous=True)  # init node
    # open serial connection
    op, ser = openPort(rospy.get_param("port"))
    rate = rospy.Rate(rospy.get_param("datarate"))
    if op:
        try:
            pubs2init = rospy.get_param("dataDesired")
            try:
                pubs = initpubs(pubs2init)  # pubs is a list of publishers
            except rospy.ROSInterruptException:
                rospy.logerr('Could not initialize publishers')
            while not rospy.is_shutdown():   
                get_pub_data(ser, pubs)
                rate.sleep()
            # is shutdown close port
            # ser.close()
        except rospy.ROSInterruptException:
            pass
    else:
        rospy.logerr('Could not open serial connection')   
