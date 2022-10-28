#! /usr/bin/env python

from typing_extensions import Annotated
import rospy
from geometry_msgs.msg import Twist



pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 
y : Annotated[float, "Unit('m/s')"]
y = 5
move = Twist() 
move.linear.y = y # conds on move.linear.x, move.linear.x defined first = no error
pub.publish(move)

rospy.spin()