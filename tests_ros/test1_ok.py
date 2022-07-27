#! /usr/bin/env python

from typing_extensions import Annotated
import rospy
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 
x : Annotated[float, "Unit('m/s')"]
x = 100

move = Twist() 
move.linear.x = x 
pub.publish(move)

rospy.spin()