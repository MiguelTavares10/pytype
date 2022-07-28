from z3 import *
from prelude import TVar, var_unit, var_value
s = Solver()

x = Const('move.linear.x',TVar)

s.add(var_value(x) > 100)
print(s.check())
print(s.model())
s.add(var_value(x) < 200)
print(s.check())
print(s.model())
s.add(var_value(x) == 150)
print(s.check())
print(s.model())