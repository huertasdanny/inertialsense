#!/usr/bin/env python

import rospy

from sensor_msgs.msg import Imu
from sensor_msgs.msg import MagneticField as Mag
from inertialsense.msg import Rawgps
from inertialsense.msg import Bar


def msg_creator(topic):
    if topic == 'GPS':
        return dummy_gps()
                    
    elif topic == 'IMU':
        return dummy_imu()
    
    elif topic == "MAG":
        return dummy_mag()

    elif topic == 'BAR':
        return dummy_bar()
    else:
        rospy.logerr('No callback for message type %s', topic)
        
def dummy_imu():
    imu_msg = Imu()
    imu_msg.header.stamp = rospy.Time.now()
    imu_msg.header.frame_id = "imu"
    imu_msg.orientation.x = 1
    imu_msg.orientation.y = 2
    imu_msg.orientation.z = 3
    imu_msg.orientation.w = 4;
    imu_msg.angular_velocity_covariance = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0];
    imu_msg.angular_velocity.x = 5;
    imu_msg.angular_velocity.y = 6;
    imu_msg.angular_velocity.z = 7;
    imu_msg.linear_acceleration_covariance = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0];
    imu_msg.linear_acceleration.x = 8;
    imu_msg.linear_acceleration.y = 9;
    imu_msg.linear_acceleration.z = 10;  
    rospy.loginfo('reading imu serial data')
    #rospy.loginfo(imu_msg)
    return imu_msg

def dummy_mag():
    mag_msg = Mag()
    mag_msg.header.stamp = rospy.Time.now() 
    mag_msg.magnetic_field.x = 11
    mag_msg.magnetic_field.y = 12
    mag_msg.magnetic_field.z = 13
    mag_msg.magnetic_field_covariance = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    rospy.loginfo('reading mag serial data')
    return mag_msg

def dummy_bar():
    bar_msg = Bar()
    bar_msg.header.stamp = rospy.Time.now()
    bar_msg.pressure = 15
    bar_msg.mslAlt = 16
    bar_msg.barTemp = 17
    bar_msg.relhmdty = 18
    rospy.loginfo('reading bar serial data')
    return bar_msg

def dummy_gps():
    gps_msg = Rawgps()
    gps_msg.header.stamp = rospy.Time.now()
    gps_msg.sat = 'Dan satellite'
    gps_msg.rcv = 18
    rospy.loginfo('reading gps serial data')
    return gps_msg
    

        