#!/usr/bin/env python
import rospy
## import sensor messages here ##
from std_msgs.msg import String

from sensor_msgs.msg import Imu
from sensor_msgs.msg import MagneticField as Mag
from inertialsense.msg import Rawgps
from inertialsense.msg import Bar


###### need to update callbacks for specific message types

def msgcallback(topic):
    if topic == 'GPS':
        return gpscallback
                    
    elif topic == 'IMU':
        return imucallback
    
    elif topic == "MAG":
        return magcallback

    elif topic == 'BAR':
        return barcallback
    else:
        rospy.logerr('No callback for message type %s', topic)
    

def gpscallback(msg):
    rospy.loginfo(rospy.get_caller_id() + 'Connected to %s satellite /n Receiver number %f', msg.sat, msg.rcv)

def imucallback(msg):
    #   ROS_INFO("Imu Seq: [%d]", msg->header.seq);
    #   ROS_INFO("Imu Orientation x: [%f], y: [%f], z: [%f], w: [%f]", msg->orientation.x,msg->orientation.y,msg->orientation.z,msg->orientation.w);
    rospy.loginfo(rospy.get_caller_id() + 'Imu Orientation x: [%f], y: [%f], z: [%f], w: [%f]', msg.orientation.x,msg.orientation.y,msg.orientation.z,msg.orientation.w)
    rospy.loginfo('Imu angular_velocity x: [%f], y: [%f], z: [%f]', msg.angular_velocity.x,msg.angular_velocity.y,msg.angular_velocity.z)
    rospy.loginfo('Imu linear_acceleration x: [%f], y: [%f], z: [%f]', msg.linear_acceleration.x,msg.linear_acceleration.y,msg.linear_acceleration.z)
    
def magcallback(msg):
    rospy.loginfo(rospy.get_caller_id() + 'MagField x:[%f], y: [%f], z: [%f]', msg.magnetic_field.x, msg.magnetic_field.y, msg.magnetic_field.z)
    
def barcallback(msg):
    rospy.loginfo(rospy.get_caller_id() + 'Bar Data /n Pressure:[%f]kPa mslAlt:[%f] /n Temp:[%f]C /n Relative Humidity:[%f]', msg.pressure, msg.mslAlt, msg.barTemp, msg.relhmdty)