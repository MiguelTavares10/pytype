from z3 import *
from run_prelude import run_prelude
from prelude import TVar, var_unit
from context_func import FuncContext

s = Solver()



contextFun = run_prelude()
# locals()["vectorX"] = getattr(contextData["Vector3"].get_data_type(),"vectorX")
# locals()["vectorY"] = getattr(contextData["Vector3"].get_data_type(),"vectorY")
# locals()["vectorZ"] = getattr(contextData["Vector3"].get_data_type(),"vectorZ")
# # Put this in fors later with strings from context and inputs
# locals()["linear"] = getattr(contextData["Twist"].get_data_type(),"linear")
# locals()["angular"] = getattr(contextData["Twist"].get_data_type(),"angular")


# ZVar = z3.RealSort()
# var_unit = z3.Function("var_u
# nit", ZVar , z3.StringSort())
# Vector3 = Datatype('Vector3')
# Twist= Datatype('Twist')



# Vector3.declare('Vector',*[('x',ZVar),('y',ZVar),('z',ZVar)])

# Twist.declare('Twist',*[('linear',Vector3),('angular',Vector3)])


# Twist, Vector3 = CreateDatatypes(Twist, Vector3)

xx = Const('x',TVar)
zz = Const('y',TVar)

print(contextFun)
move = Const('move', contextFun["Twist"].get_data_type())

# linear = Twist.linear

# angular = Twist.angular

# vectorX = Vector3.x

# vectorZ = Vector3.z

s.add(var_unit(xx) == z3.StringVal("m/s"))
s.add(var_unit(zz) == z3.StringVal("degrees/s"))
prop = var_unit(contextFun["Twist"].get_data("vectorX",contextFun)(contextFun["Twist"].get_data("linear",contextFun)(move))) == z3.StringVal("m/s")

print(prop)
s.add(prop)
prop2 = var_unit(contextFun["Twist"].get_data("vectorZ",contextFun)(contextFun["Twist"].get_data("angular",contextFun)(move))) == z3.StringVal("rad/s")
s.add(prop2)

print(s.check())
print(s.model())
s.add(var_unit(xx) == var_unit(contextFun["Twist"].get_data("vectorX",contextFun)(contextFun["Twist"].get_data("linear",contextFun)(move))))
print(s.check())
print(s.model())
s.add(var_unit(zz) == var_unit(contextFun["Twist"].get_data("vectorZ",contextFun)(contextFun["Twist"].get_data("angular",contextFun)(move))))


print(s.check())