import rospy
import serial
import sys
sys.path.append(r'/home/catkin_ws/src/inertialsense/src/scripts')
import checksum
from serial import SerialException
from std_msgs.msg import String
from sensor_msgs.msg import Imu


if __name__ == '__main__':    
    rospy.init_node('is_dataparser', anonymous=True) #init node
    #open serial connection
    op,ser = openPort(rospy.get_param("port"))
    if op:
        try:
            pubs2init = rospy.get_param("desiredata")
            possPub = rospy.get_param("possdata")
            pubs = initpubs(pubs2init, possPub) #pubs is a list of publishers
            get_pub_data(ser, pubs)
        except rospy.ROSInterruptException:
            pass
    else:
        rospy.logerr('Could not open serial connection')   

def openPort(port_settings):
    ser = serial.Serial(timeout = port_settings.tout)
    possports = port_settings.pname
    ser.baudrate = port_settings.baud
    # iterrate through possible ports trying to connect
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
        msgs,msgtypes = IS_raw2msg(ser)
        ## possible for there to be less messages than publishers but not other way around
        if len(msgs) > len(pubs):
            rospy.logerr('Too many messages')
        else:
            for i in msgtypes:
                if i == 0: #GPS
                    try:
                        pubs.gps.publish(msgs.gps)
                    except rospy.ROSException:
                        rospy.logerr('No GPS publisher initialized')
                if i == 1: #IMU
                    try:
                        pubs.gps.publish(msgs.imu)
                    except rospy.ROSException:
                        rospy.logerr('No IMU publisher initialized')
                if i == 2: #MAG
                    try:
                        pubs.gps.publish(msgs.mag)
                    except rospy.ROSException:
                        rospy.logerr('No MAG publisher initialized')
                if i == 3: #BAR
                    try:
                        pubs.gps.publish(msgs.bar)
                    except rospy.ROSException:
                        rospy.logerr('No BAR publisher initialized')
        rate.sleep()
    #is shutdown close port
    #ser.close()
def initpubs(desired, possible):
    pubs = dict()
    msgtypes = []
    #check possible
    if  possible != ['GPS','IMU','MAG','BAR']: 
        rospy.logerr('Mismatched possible IS messages, make sure order in .launch is the same as under IS_msgsub initpub')
        return pubs,msgstypes
    for i in desired:
        if i == 0:
            pubs.gps = rospy.Publisher('IS_GPS', Gps, queue_size=10)
        elif i==1:
            pubs.imu = rospy.Publisher('IS_IMU', Imu, queue_size=10)
        elif i==2:
            pubs.mag = rospy.Publisher('IS_MAG', Mag, queue_size=10)
        elif i==3:
            pubs.bar = rospy.Publisher('IS_BAR', Bar, queue_size=10)
        else:
            rospy.logerr('Unknown desired publisher %f', i)
            return dict(), [] #unknown desired publisher
        msgtypes.append(i)
    return pubs,msgstypes