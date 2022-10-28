#! /usr/bin/env python

from typing_extensions import Annotated
import rospy
from geometry_msgs.msg import Twist



pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 
x : Annotated[float, "Unit('m/s')"]
z : Annotated[float, "Unit('m/s')"]
x = 2
z = 5
move = Twist() 
move.linear.x = x + z
pub.publish(move)

rospy.spin()