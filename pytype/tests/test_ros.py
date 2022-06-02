"""Tests for PEP-593 typing.Annotated types."""

from pytype import file_utils
from pytype.tests import test_base


class ROSTest(test_base.BaseTest):
  """Tests for typing.Annotated types."""  
  
  def test_basic(self):
    ty = self.Infer("""
      from typing_extensions import Annotated
      i = ... # type: Annotated[int, "foo"]
      s: Annotated[str, "foo", "bar"] = "baz"
    """)
    self.assertTypesMatchPytd(ty, """
      i: int errado
      s: str
    """)
