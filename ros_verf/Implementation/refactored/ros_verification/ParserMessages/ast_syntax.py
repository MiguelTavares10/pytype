class Node:
    pass

class Literal:
    ##Receber tipo de literal e fazer o self.type
    def __init__(self,value,typeLit):
        self.valuestr = value
        self.value = value
        self.type = str
        if typeLit == 'INT_LIT':
            self.value = int(value)
            self.type = int
        elif typeLit == 'FLOAT_LIT':
            self.value = float(value)
            self.type = float
        elif typeLit == 'BOOL_LIT':
            self.value = bool(value)
            self.type = bool
        elif typeLit == 'STRING_LIT':
            pass
        else:
            raise Exception("Error when parsing literal:", value)


    def get_value(self):
        return self.value

    def get_type(self):
        return self.type

    def __str__(self):
        return self.valuestr
class Minus:
    
    def __init__(self,args):
        self.var = args[0]
        
    def __str__(self):
        return "( - " + self.var +  ")"

class Variable:
    def __init__(self,name):
        self.name = name

    def get_var_name(self):
        return self.name
    
    def __str__(self):
        return self.name

class ClassVariable:

    def __init__(self,name):
        self.name = name[0]
        for n in name[1:]:
            self.name += "." + n
     
    def get_var_name(self):
        return self.name
    
    def __str__(self):
        return self.name     


class LogicalExpression:
    def __init__(self,left,operador,right):
            self.left = left
            self.operador = operador
            self.right = right
            
    def get_left_side(self):
        return self.left
    
    def get_operador(self):
        return self.operador

    def get_right_side(self):
        return self.right
    
    def __str__(self):
        return self.left.__str__() + " " + self.operador + " " + self.right.__str__()


class IfExpression:
    def __init__(self,vBool,vTrue,vFalse):
            self.question = vBool
            self.truePart = vTrue
            self.falsePart = vFalse

    def get_question(self):
        return self.question
    
    def get_true_part(self):
        return self.truePart

    def get_false_part(self):
        return self.falsePart
    def __str__(self):
        return "If " + self.question + " then " + self.truePart + " else " + self.falsePart

    
class Condition:
    def __init__(self,left,operator,right):

            if isinstance(left, Variable) or isinstance(left,ClassVariable):
                self.left = "var_value ( " + left.__str__() + " )"
            else:
                self.left = left
            if isinstance(right, Variable) or isinstance(right,ClassVariable):
                self.right = "var_value ( " + right.__str__() + " )"
            else:
                self.right = right
            self.operador = operator

    
    def get_left_side(self):
        return self.left
    
    def get_operador(self):
        return self.operador

    def get_right_side(self):
        return self.right

    def get_cond(self):
        return self.left + self.operador + self.right

    def __str__(self):
        return self.left.__str__() + " " + self.operador + " "+  self.right.__str__()

class FunctionExpression:
    def __init__(self,args):
        self.args = args[1:-2]
        self.name = args[0]
        self.left = args[-1]
        self.op = args[-2]
    
    def get_args(self):
        return self.args

    def get_name(self):
        return self.name
    
    def get_operator(self):
        return self.op

    def get_left_side(self):
        return self.left

    def __str__(self):
        stringArgs = ""
        for arg in self.get_args():
            stringArgs += str(arg) + ","
        stringArgs = stringArgs[:-1]
        return "Fun " + self.name + "(" + stringArgs + ") " + self.op + " " + self.left

class AritmeticExpression:
    def __init__(self,left,operador,right):
            self.left = left
            self.operador = operador
            self.right = right
    
    def get_left_side(self):
        return self.left
    
    def get_operador(self):
        return self.operador

    def get_right_side(self):
        return self.right

    def __str__(self):
        return self.left.__str__() + self.operador + self.right.__str__()