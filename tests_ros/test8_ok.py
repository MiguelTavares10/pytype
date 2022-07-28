#! /usr/bin/env python

from typing_extensions import Annotated
import rospy
from geometry_msgs.msg import Twist



pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 
x : Annotated[float, "Unit('m/s')"]
x = 5
move = Twist() 
move.linear.x = x # conds on move.linear.x, move.linear.x defined first = no error
pub.publish(move)

rospy.spin()