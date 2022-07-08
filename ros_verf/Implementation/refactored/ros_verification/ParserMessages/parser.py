from lark import Lark, Transformer, v_args
import os
from .ast_syntax import LogicalExpression, IfExpression, Condition, Literal, Variable,FunctionExpression, AritmeticExpression, ClassVariable

class TreeToROS(Transformer):
        def __init__(self):
                super().__init__()
                self.vars = {}

        def start(self,args):
                return args[0]
        
        def expr(self,args):
                return args[0]

        def expr_log(self,args):
                return LogicalExpression(args[0],args[1],args[2])

        def expr_if(self,args):
                return IfExpression(args[0],args[1],args[2])


        def expr_bool(self,args):
                return Condition(args[0],args[1],args[2])

        def expr_arit(self,args):
                return AritmeticExpression(args[0],args[1],args[2])


        def expr_fun(self,args):
                return FunctionExpression(args)               

        def expr_literal(self,args):
                return Literal(args[0].value,args[0].type)

        def expr_var(self,args):
                if len(args) == 1:
                        return Variable(args[0])
                else:
                        return ClassVariable(args)

        # def expr_bracket(self,args):
        #         return args[0]

        # def expr_unop(self,args):
        #         return args[0]

# Creation of the parser
def mk_parser(rule="start"):
    return Lark.open(
        "./ros_verf/Implementation/refactored/ros_verification/ParserMessages/grammar.lark",
        parser='lalr',
        #lexer='standard',
        start=rule,
        transformer=TreeToROS())

def parse_comments(file):
        
        folder = "./ros_verf/Implementation/refactored/ros_verification/ROSMessages"
        result = []
        caminho = f"{folder}/{file}.msg"
        #caminho = file +".msg"
        if os.path.isfile(caminho) :
                print(f"{caminho} é ficheiro")

                readFile = open(caminho, "r")

                lines = readFile.readlines()
                
                result = []

                for line in lines:
                        if line.__contains__("#RobotFix#"):
                                splitLine = line.split("#RobotFix#")
                                for sLine in splitLine[1:]:
                                        result.append(sLine)
 
                return result
        print("não é ficheiro")
        return []
