#! /usr/bin/env python

from typing_extensions import Annotated
import rospy
from geometry_msgs.msg import Twist

move = Twist()

move.linear.x = 1

move2 = Twist()
move2.linear.x = 2

x : Annotated[float,"Unit('m/s')"]
x = move.linear.x 

y : Annotated[float,"Unit('m/s') and y == x"]
y = move2.linear.x
rospy.spin()