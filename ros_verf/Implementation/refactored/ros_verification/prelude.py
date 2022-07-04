import z3

        


TVar = z3.RealSort()
var_unit = z3.Function("var_unit", TVar , z3.StringSort())
var_value = z3.Function("var_value",TVar,z3.RealSort())