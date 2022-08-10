#! /usr/bin/env python

from typing_extensions import Annotated
import rospy
from geometry_msgs.msg import Twist



pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 
move = Twist()
move.linear.x = 100
move.linear.y = 100
move.linear.z = 100
pub.publish(move)

rospy.spin()