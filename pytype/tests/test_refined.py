"""Tests for refined types"""

from pytype.tests import test_base


class TestRefined(test_base.BaseTest):
  """Tests for refined types."""

  def test_refined_simple(self):
    self.Check("""
      from typing_extensions import Annotated
      import rospy
      from sensor_msgs.msg import LaserScan
      from geometry_msgs.msg import Twist
      move = Twist()
      x: Annotated[int,"#Unit(m/s) && _ > 0"]
      y: Annotated[int,"#Unit(m/s)"]
      x = 1
      z: Annotated[int,"_ < 20 && #Unit(rads/s)"]
      z = 10
      x = 2
      y = 15
      z = x 
    """)

if __name__ == "__main__":
  test_base.main()