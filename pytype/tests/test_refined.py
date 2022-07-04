"""Tests for refined types"""

from pytype.tests import test_base


class TestRefined(test_base.BaseTest):
  """Tests for refined types."""

  def test_refined_simple(self):
    self.Check("""
      from typing_extensions import Annotated
      x: Annotated[int, "_ > 0"]
      y: Annotated[int, "_ > 1"]
      x = 1 + 1
      z: Annotated[int,"_ < 10"]
      z = 5
      x = 10
      y = 15
      z = x
      
    """)
    

    

if __name__ == "__main__":
  test_base.main()