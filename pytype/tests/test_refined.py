"""Tests for refined types"""

from pytype.tests import test_base


class TestRefined(test_base.BaseTest):
  """Tests for refined types."""

  def test_refined_simple(self):
    self.Check("""
      from typing_extensions import Annotated
      import rospy
      from geometry_msgs.msg import Twist

      move = Twist() 
      x : Annotated[int,"#Unit(rad/s)"] 
      x = 2
      move.linear.y = 15
      move.angular.x = x
    """)

if __name__ == "__main__":
  test_base.main()