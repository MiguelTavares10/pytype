#! /usr/bin/env python

from typing_extensions import Annotated
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def test():
    test = 1

def callback(msg : LaserScan):
    

    x : Annotated[float, "Unit('m/s')"]
    z : Annotated[float, "Unit('m/s') and _ < 100"]

    if msg.ranges[360] > 1:
        x = 1
        z = 0

    if msg.ranges[360] < 1:
        x = 0.1
        z= 60

    if msg.ranges[719] < 0.4:
        x = 0.1
        z= 50

    if msg.ranges[0] < 0.4:
        x = 0.1
        z= 50


    move.linear.x = x 
    move.angular.z = z 
    pub.publish(move)


test()
v : Annotated[float, "Unit('rad/s') and _ > 0"]
v = 1.0
rospy.init_node('pub_sub_node')
move = Twist() 
move.angular.x = v
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan , callback)

#msg = LaserScan()
#callback(msg)
#('LOAD_NAME', 42, 'LaserScan') run op in block type op = <class 'pytype.pyc.opcodes.LOAD_NAME'> op.index = 45 op.arg = 4 , op.line = 42 op.pretty_arg = LaserScan
#('CALL_FUNCTION', 42, 'unsolveable') run op in block type op = <class 'pytype.pyc.opcodes.CALL_FUNCTION'> op.index = 46 op.arg = 0 , op.line = 42 op.pretty_arg = 0
#('STORE_NAME', 42, 'msg') run op in block type op = <class 'pytype.pyc.opcodes.STORE_NAME'> op.index = 47 op.arg = 12 , op.line = 42 op.pretty_arg = msg
#('LOAD_NAME', 43, 'callback') run op in block type op = <class 'pytype.pyc.opcodes.LOAD_NAME'> op.index = 48 op.arg = 8 , op.line = 43 op.pretty_arg = callback
#('LOAD_NAME', 43, 'msg') run op in block type op = <class 'pytype.pyc.opcodes.LOAD_NAME'> op.index = 49 op.arg = 12 , op.line = 43 op.pretty_arg = msg
#('CALL_FUNCTION', 43, 'callback') run op in block type op = <class 'pytype.pyc.opcodes.CALL_FUNCTION'> op.index = 50 op.arg = 1 , op.line = 43 op.pretty_arg = 1
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 


rospy.spin()

