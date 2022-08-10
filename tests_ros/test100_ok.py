#! /usr/bin/env python

from typing_extensions import Annotated
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg : LaserScan):
    
    move = Twist() 
    x : Annotated[float, "Unit('m/s')"]
    z : Annotated[float, "Unit('rad/s') and _ < 100"]
    x = 1
    z = 2
    move.linear.x = 100
    move.linear.x = x 
    move.angular.z = z 
    pub.publish(move)


rospy.init_node('pub_sub_node')
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan , callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 


rospy.spin()
