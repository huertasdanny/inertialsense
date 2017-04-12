#!/usr/bin/env python
import rospy

import sys
sys.path.append(r'/home/catkin_ws/src/inertialsense/src/scripts')
from init_pub_sub import initsub


#Subscriber node for IS Messages


def listener(subs2init):

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.    
    
    initsub(subs2init)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    subs2init = rospy.get_param("dataDesired")
    rospy.init_node('IS_msgsubscriber', anonymous=True)
    listener(subs2init)