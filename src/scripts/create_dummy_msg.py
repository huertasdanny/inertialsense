#!/usr/bin/env python

import rospy

from sensor_msgs.msg import Imu
from sensor_msgs.msg import MagneticField as Mag
from inertialsense.msg import Rawgps
from inertialsense.msg import Bar


class dummy_msg():
    def __init__(self):
        
            
            
    def dummy_imu(self):
        imu_msg = Imu()
        imu_msg.header.stamp = rospy.Time.now()
        imu_msg.header.frame_id = "imu"
        imu_msg.orientation.x = 1
        imu_msg.orientation.y = 2
        imu_msg.orientation.z = 3
        imu_msg.orientation.w = 4;
        //imu_msg.angular_velocity_covariance = {0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0};
        imu_msg.angular_velocity.x = 5;
        imu_msg.angular_velocity.y = 6;
        imu_msg.angular_velocity.z = 7;
        //imu_msg.angular_velocity_covariance = {0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0};
        imu_msg.linear_acceleration.x = 8;
        imu_msg.linear_acceleration.y = 9;
        imu_msg.linear_acceleration.z = 10;  
        return imu_msg
    
    def dummy_mag(self):
        mag_msg = Mag()
        mag_msg.header.stamp = rospy.Time.now() 
        mag_msg.magnetic_field(11,12,13);
        mag_msg.magnetic_field_covariance(0)
        mag_msg.header.stamp = rospy.Time.now()
        return mag_msg
    
    def dummy_bar(self):
        bar_msg = Bar(14,15,16,17)
        bar_msg.header.stamp = rospy.Time.now()
        return bar_msg
    
    def dummy_gps(self):
        gps_msg = Rawgps()
        gps_msg.header.stamp = rospy.Time.now()
        gps_msg.sat = 'Dan satellite'
        gps_msg.rcv = 18
        return gps_msg
        

        