#!/usr/bin/env python

import rospy
from init_pub_sub import initpubs
import IS_raw2msg
import serial
import sys
sys.path.append(r'/home/catkin_ws/src/inertialsense/src/scripts')
from serial import SerialException


def openPort(port_settings):
    ser = serial.Serial(timeout = port_settings.tout)
    possports = port_settings.pname
    ser.baudrate = port_settings.baud
    # iterate through possible ports trying to connect
    for port in possports:
        ser.port = port
        try:
            ser.close()
            ser.open()
            return 1, ser
        except SerialException:
            pass
    return 0,ser


def get_pub_data(ser, pubs):
    rate = rospy.Rate(rospy.get_param("datarate"))
    while not rospy.is_shut_down():
        msgs = IS_raw2msg(ser)
        ## have msgs be dictionary of messages 
        ## possible for there to be less messages than publishers but not other way around
        if len(msgs) > len(pubs):
            rospy.logerr('Too many messages')
        else:
            for msg in msgs.keys():
                if msg == 'GPS':
                    try:
                        pubs.gps.publish(msgs.GPS)
                    except rospy.ROSException:
                        rospy.logerr('No GPS publisher initialized')
                if msg == 'IMU':
                    try:
                        pubs.gps.publish(msgs.IMU)
                    except rospy.ROSException:
                        rospy.logerr('No IMU publisher initialized')
                if msg == 'MAG':
                    try:
                        pubs.gps.publish(msgs.MAG)
                    except rospy.ROSException:
                        rospy.logerr('No MAG publisher initialized')
                if msg == 'BAR':
                    try:
                        pubs.gps.publish(msgs.BAR)
                    except rospy.ROSException:
                        rospy.logerr('No BAR publisher initialized')
        rate.sleep()
    #is shutdown close port
    #ser.close()
    
if __name__ == '__main__':    
    rospy.init_node('is_dataparser', anonymous=True) #init node
    #open serial connection
    op,ser = openPort(rospy.get_param("port"))
    if op:
        try:
            pubs2init = rospy.get_param("dataDesired")
            try:
                pubs = initpubs(pubs2init) #pubs is a list of publishers
            except rospy.ROSInterruptException:
                rospy.logerr('Could not initialize publishers')
                
            get_pub_data(ser, pubs)
        except rospy.ROSInterruptException:
            pass
    else:
        rospy.logerr('Could not open serial connection')   