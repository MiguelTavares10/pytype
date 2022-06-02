import textwrap
from pytype.pyi import parser
from pytype.ast import visitor as ast_visitor
import sys
if sys.version_info >= (3, 8):
  import ast as ast3
else:
  from typed_ast import ast3

def parse(src, name=None, version=None, platform="linux"):
    # if version:
    #     self.options.python_version = version
    # self.options.platform = platform
    # version = version or self.python_version
    src = textwrap.dedent(src).lstrip()
    ast = parser.parse_string(src, name=name)
    return ast

expected = """
    from typing import Annotated

    class A:
        name: Annotated[str, 'property']
    """

p = parse(expected)

print(p)

an = ast_visitor.BaseVisitor(ast3)
an.visit(p)


