"""Tests for refined types"""

from pytype.tests import test_base
import os


class TestRefined(test_base.BaseTest):
  """Tests for refined types."""

  # def test_refined_simple(self):
  #   self.Check("""
  #     from typing_extensions import Annotated
  #     import rospy
  #     from geometry_msgs.msg import Twist

  #     move = Twist() 
  #     x : Annotated[int,"#Unit(rad/s)"] 
  #     x = 2
  #     move.linear.y = 15
  #     move.angular.x = x
  #   """)


  def test_refined_file(self):
    folder = "./"
    file = "simple_pub_sub.py"
    result = []
    caminho = f"{folder}/{file}"
    #caminho = file +".msg"
    if os.path.isfile(caminho) :
            print(f"{caminho} é ficheiro")

            readFile = open(caminho, "r")

            lines = readFile.readlines()
            code = ""
            for line in lines:
              code +=line
    
    self.Check(code)


if __name__ == "__main__":
  test_base.main()