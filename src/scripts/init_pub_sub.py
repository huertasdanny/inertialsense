#!/usr/bin/env python
import rospy
## import sensor messages here ##
from std_msgs.msg import String

from sensor_msgs.msg import Imu
from sensor_msgs.msg import MagneticField as Mag
from inertialsense.msg import Rawgps
from inertialsense.msg import Bar

def initpubs(pubs):
    
    ## instead have desired be a dictionary whose fields are the message types, 
    #find which fields have a true field and create those publishers. return dictionary of publishers
    publishers = {}
    for topic, publish in pubs.items():
        if publish:
            if topic == 'GPS':
                publishers.gps = rospy.Publisher('IS_GPS', Rawgps, queue_size=10)
            elif topic == 'IMU':
                publishers.imu = rospy.Publisher('IS_IMU', Imu, queue_size=10)
            elif topic == "MAG":
                publishers.mag = rospy.Publisher('IS_MAG', Mag, queue_size=10)
            elif topic == 'BAR':
                publishers.bar = rospy.Publisher('IS_BAR', Bar, queue_size=10)
            else:
                rospy.logerr('Desired topic %s has not been configured', topic)
    
    return publishers



def initsub(subs):
    #subs is a dictionary of topic: bool pairs where bool is whether or not to subscribe to topic
    for topic, subscribe in subs.items():
        if subscribe:
            if topic == 'GPS':
                rospy.Subscriber('IS_GPS', Rawgps, gpscallback)
            elif topic == 'IMU':
                rospy.Subscriber('IS_IMU', Imu, imucallback)
            elif topic == "MAG":
                rospy.Subscriber('IS_MAG', Mag, magcallback)
            elif topic == 'BAR':
                rospy.Subscriber('IS_BAR', Bar, barcallback)
            else:
                rospy.logerr('Desired topic %s has not been configured', topic)

###### need to update callbacks for specific message types
def gpscallback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)

def imucallback(data):
    #   ROS_INFO("Imu Seq: [%d]", msg->header.seq);
    #   ROS_INFO("Imu Orientation x: [%f], y: [%f], z: [%f], w: [%f]", msg->orientation.x,msg->orientation.y,msg->orientation.z,msg->orientation.w);
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)
    
def magcallback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)
def barcallback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)
#######################
    