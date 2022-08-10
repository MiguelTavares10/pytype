#! /usr/bin/env python

from typing_extensions import Annotated
import rospy
from geometry_msgs.msg import Twist



pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 
move = Twist()
x : Annotated[float, "Unit('m/s')"]
move.linear.x = 1
x = move.linear.x
pub.publish(move)

rospy.spin()