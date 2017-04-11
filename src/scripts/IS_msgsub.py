import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import String


#Subscriber node for IS Messages



    
def initsub(desired,possible):
    #check possible
    if  possible != ['GPS','IMU','MAG','BAR']: 
        rospy.logerr('Mismatched possible INS messages, make sure order in launch is the same as under IS_msgsub initsub')
        return 0
    for i in desired:
        if i == 0:
            rospy.Subscriber('IS_GPS', Gps, gpscallback)
        elif i==1:
            rospy.Subscriber('IS_IMU', Imu, imucallback)
        elif i==2:
            rospy.Subscriber('IS_MAG', Mag, magcallback)
        elif i==3:
            rospy.Subscriber('IS_BAR', Bar, barcallback)
        else:
            return 0
    return 1

###### need to update callbacks for specific message types
def gpscallback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)

def imucallback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)
    
def magcallback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)
def barcallback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)
#######################
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.    
    subs2init = rospy.get_param("desiredata")
    possSub = rospy.get_param("possdata")
    initsub(subs2init, possSub)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    
    rospy.init_node('IS_msgsub', anonymous=True)
    listener()