from asyncio import constants
import textwrap
from pytype.pyi.AnnotationHandler import AnnotationHandler
from pytype.pyi import parser
from pytype.ast import visitor as ast_visitor
from pytype.directors import parse_src
from pytype.vm import VirtualMachine
from pytype import load_pytd
from pytype import context
from pytype import preprocess
from pytype import config
import sys
from pytype import context
from pytype.tests import test_utils

from verification import Verification
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
    
options = config.Options.create(
    python_version=(3,8),
    build_dict_literals_from_kwargs=True,
    enable_bare_annotations=True,
    enable_cached_property=True,
    overriding_default_value_checks=True,
    overriding_parameter_count_checks=True,
    overriding_parameter_name_checks=True,
    overriding_parameter_type_checks=True,
    overriding_return_type_checks=True,
    strict_namedtuple_checks=True,
    strict_parameter_checks=True,
    strict_primitive_comparisons=True,
    use_enum_overlay=True)

loader = load_pytd.create_loader(options)
context = context.Context(options=options, loader=loader)
v = Verification()
expected = """
from typing import Annotated
class A:

    x: Annotated[int,'x>0']
    y: Annotated[int,'y<0']
    
    def __init__(self):
        a = 1
"""
vm = VirtualMachine(context)
# src = preprocess.augment_annotations(expected)
# print(f"augment annotation = {src}")
# src = parse_src(src,(3,8))
# print(f"parse_src = {src}")
# lines = expected.split("\n")
op = test_utils.FakeOpcode("foo.py", 123, "foo")
vm.trace_opcode(op, "x", 42)
result = vm.run_program(expected, "",100)
pg = result[0].program
print(dir(pg))
for node in pg.cfg_nodes:
  print(f"node = {node.program.cfg_nodes[0].program} dir = {dir(node.program)}")

# for line in lines:
#   p = parse(line)
#   print(p)
#   v.check_node(p)


#an = ast_visitor.BaseVisitor(ast3)
#an.visit(p)


