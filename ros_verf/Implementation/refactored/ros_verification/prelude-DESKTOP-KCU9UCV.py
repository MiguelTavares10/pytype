import z3

from ros_verification.dsl import StrLit

TVar = z3.RealSort()
var_unit = z3.Function("var_unit", TVar , z3.StringSort())
Vector3 = z3.Datatype('Vector3')
Twist= z3.Datatype('Twist')

Vector3.declare('Vector',('x',TVar),('y',TVar),('z',TVar))

Twist.declare('Twist',('linear',Vector3),('angular',Vector3))

Twist, Vector3 = z3.CreateDatatypes(Twist, Vector3)

var_unit = z3.Function("var_unit", TVar , z3.StringSort() )