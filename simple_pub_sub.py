#! /usr/bin/env python

from typing_extensions import Annotated
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def test():
    test = 1

def callback():
    move = Twist() 
    msg : LaserScan = LaserScan()

    x : Annotated[float, "Unit('m/s')"]
    z : Annotated[float, "Unit('m/s') and _ < 100"]

    if msg.ranges[360] > 1:
        x = 1
        z = 0

    if msg.ranges[360] < 1:
        x = 0.1
        z= 60

    if msg.ranges[719] < 0.4:
        x = 0.1
        z= 50

    if msg.ranges[0] < 0.4:
        x = 0.1
        z= 50


    move.linear.x = x 
    move.angular.z = z 
    pub.publish(move)


rospy.init_node('pub_sub_node')

sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan , callback)

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 


rospy.spin()


test()
