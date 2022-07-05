import textwrap

from pytype import blocks
from pytype import context
from pytype import utils
from pytype import vm
from pytype.pyc import opcodes
from pytype.pyc import pyc
from pytype.tests import test_base
from pytype.tests import test_utils


# The tests in this file check disassembled bytecode, which varies from version
# to version, so we fix the test version.
_OPMAP = {v.__name__: k for k, v in opcodes.python_3_7_mapping.items()}

class VmTestBase(test_base.BaseTest, test_utils.MakeCodeMixin):
  """Base for VM tests."""
  def __init__(self):
    super()

  def setUp(self):
    super().setUp()
    self.ctx = self.make_context()

  def make_context(self):
    return context.Context(options=self.options, loader=self.loader)

class AnnotationsTest(VmTestBase):
  def __init__(self):
    super()
  """Tests for recording annotations."""
  def test_record_local_ops(self):
    self.ctx.vm.run_program("v: int = None", "", maximum_depth=10)
    self.assertEqual(
        self.ctx.vm.local_ops, {
            "<module>": [
                vm.LocalOp(name="v", op=vm.LocalOp.ASSIGN),
                vm.LocalOp(name="v", op=vm.LocalOp.ANNOTATE)
            ]
        })

  def my_test(self):
    expected = """
from typing_extensions import Annotated
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
move = Twist()
y: Annotated[int,"#Unit(m/s)"]
y = 15
move.linear.y = y

move.angular.y = y
"""
    node, glb_members = self.ctx.vm.run_program(expected, "", maximum_depth=10)
    actual = [(op.name, op.line, symbol)
              for op, symbol, _ in self.ctx.vm.opcode_traces]
    for act in actual:
      print(act)


if __name__ == "__main__":
  tb = VmTestBase()
  an = AnnotationsTest()
  an.setUpClass()
  an.setUp()
  an.my_test()