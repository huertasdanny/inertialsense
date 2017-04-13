#!/usr/bin/env python
import rospy
## import sensor messages here ##
from std_msgs.msg import String

from sensor_msgs.msg import Imu
from sensor_msgs.msg import MagneticField as Mag
from inertialsense.msg import Rawgps
from inertialsense.msg import Bar
from IS_msgcallback import msgcallback

def initpubs(pubs):
    rospy.loginfo('initializing publishers')
    ## instead have desired be a dictionary whose fields are the message types, 
    #find which fields have a true field and create those publishers. return dictionary of publishers
    publishers = {}
    for topic, publish in pubs.items():
        #print 'Publish to', topic,'?', publish
        if publish:
            try:
                if topic == 'GPS':
                    publishers[topic] = rospy.Publisher('IS_GPS', Rawgps, queue_size=10)
                    rospy.loginfo('Initialized %s Publisher', topic)
                elif topic == 'IMU':
                    publishers[topic] = rospy.Publisher('IS_IMU', Imu, queue_size=10)
                    rospy.loginfo('Initialized %s Publisher', topic)
                elif topic == "MAG":
                    publishers[topic] = rospy.Publisher('IS_MAG', Mag, queue_size=10)
                    rospy.loginfo('Initialized %s Publisher', topic)
                elif topic == 'BAR':
                    publishers[topic] = rospy.Publisher('IS_BAR', Bar, queue_size=10)
                    rospy.loginfo('Initialized %s Publisher', topic)
                else:
                    rospy.logerr('Desired topic %s has not been configured', topic)
            except rospy.ROSException:
                rospy.logerr('Could not initialize %s Publisher', topic)
    
    return publishers



def initsub(subs):
    rospy.loginfo('initializing subscribers')
    #print(subs)
    #subs is a dictionary of topic: bool pairs where bool is whether or not to subscribe to topic
    for topic, subscribe in subs.items():
        #print 'Subscribe to', topic,'?', subscribe
        if subscribe:
            try:
                if topic == 'GPS':
                    rospy.Subscriber('IS_GPS', Rawgps, msgcallback(topic))
                    rospy.loginfo('Initialized %s Subscriber', topic)
                elif topic == 'IMU':
                    rospy.Subscriber('IS_IMU', Imu, msgcallback(topic))
                    rospy.loginfo('Initialized %s Subscriber', topic)
                elif topic == "MAG":
                    rospy.Subscriber('IS_MAG', Mag, msgcallback(topic))
                    rospy.loginfo('Initialized %s Subscriber', topic)
                elif topic == 'BAR':
                    rospy.Subscriber('IS_BAR', Bar, msgcallback(topic))
                    rospy.loginfo('Initialized %s Subscriber', topic)
                else:
                    rospy.logerr('Desired topic %s has not been configured', topic)
               
            except rospy.ROSException:
                rospy.logerr('Could not subscribe to Inertial Sense data')
                
    
