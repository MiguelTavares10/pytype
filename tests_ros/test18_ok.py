#! /usr/bin/env python

from typing_extensions import Annotated
import rospy
from geometry_msgs.msg import Twist



pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 
x : Annotated[float, "Unit('rad/s')"]
z : Annotated[float, "Unit('rad/s')"]
x = 10
z = 60
move = Twist()
move.linear.x = 1
ang : Annotated[float,"Unit('rad/s') and _ > 0"] 
ang = x + z
move.angular.z = ang
pub.publish(move)

rospy.spin()