#! /usr/bin/env python

from typing_extensions import Annotated
import rospy
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 
x : Annotated[float, "Unit('m/s')"]
z : Annotated[float, "Unit('m/s')"]
y : Annotated[float, "Unit('m/s') and _ > 0 and _ < 20"]
x = 10
z = 5
y = x + z
move = Twist() 
move.linear.x = y
pub.publish(move)

rospy.spin()