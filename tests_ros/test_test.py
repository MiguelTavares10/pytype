#! /usr/bin/env python

from typing_extensions import Annotated
import rospy
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 
x : Annotated[float, "Unit('m/s')"]
x = 5

move = Twist() 
move.linear.x : Annotated[float,"Unit('m/s') and _ > 0 and _ > 5"]
move.linear.x = 5 
pub.publish(move)

rospy.spin()