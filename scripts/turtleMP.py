#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def Init():
    rospy.init_node('turtleMP')
    pub = rospy.Publisher('cmd_MP', Twist, queue_size=1)

def callback(data):
    #rospy.init_mode["listenerMP"]
    rospy.loginfo("X [%f], Y [%f], Z [%f], angle [%d]", data.linear.x, data.linear.y, data.linear.z, data.angular.x)
    pub = rospy.Publisher('cmd_MP', Twist, queue_size=1)
    data.linear.x=15*data.linear.x
    pub.publish(data)

def listener():
    rospy.Subscriber('cmd_GB', Twist, callback)
    rospy.spin()   # empeche le script de s'eteindre

if __name__=='__main__':
    Init()
    listener()
