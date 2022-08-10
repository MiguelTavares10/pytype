from z3 import *

from ros_verf.Implementation.refactored.ros_verification.prelude import TVar
from ros_verf.Implementation.refactored.ros_verification.dsl import VFunction 
from ros_verf.Implementation.refactored.ros_verification.prelude import var_unit, var_value, TVar
from ros_verf.Implementation.refactored.ros_verification.ParserMessages.ast_syntax import LogicalExpression, IfExpression, Condition, Literal, Variable,FunctionExpression, AritmeticExpression

COMMAND_LINE_BRACKETS = "###################################################################################"
base_types = ["float64","uint32","string","int32"]
def transform_name(name):
        if name == "x":
                return "vectorX"
        if name == "y":
                return "vectorY"
        if name == "z":
                return "vectorZ"
        return name

def build_var_type(vName, vType, context):
        if vType == "float64":
                return TVar
        elif vType == "int32":
                return TVar
        elif vType == "uint32":
                return TVar
        elif vType == "string":
                return z3.StringSort()
        elif vType in context:
                if isinstance(context[vType],FuncContext):
                        return context[vType].get_data_type()
        else:
                return vType

class FieldFunc:


        def __init__(self,name,typ):
                self.name = name
                self.typ = typ
                self.data = ""
        
        def get_name(self):
                return self.name
        
        def get_typ(self):
                return self.typ
        
        def add_data(self,data):
                self.data = data

        def get_data(self):
                return self.data


class FuncContext:
        def __init__(self,name,vars,context):
                newVars = []
                self.fields = []
                varFields = vars.fields
                for var in varFields:
                        varName = transform_name(var.name)
                        varType = var.typ
                        varTypeSplit = varType.split("/")
                        varType = varTypeSplit[-1]
                        self.fields.append(FieldFunc(varName,varType))
                        newVarType = build_var_type(varName,varType,context)
                        newVars.append((varName, newVarType))
                
                print(f"self.fields = {self.fields}")

                self.dataType = z3.Datatype(transform_name(name))
                self.name = transform_name(name)
                print(f"name = {name} newVars = {newVars}")
                self.dataType.declare(name,*newVars)       
                self.conds = []
                self.annotations = [] 
                self.func = "Nenhuma"
                self.keep_func = "Nenhuma"
                self.constsFunc = {}
                self.save_inputCond = ""
                self.keep_done_conditions = ""



        def get_name(self):
                return self.name


        def get_data_type(self):
                return self.dataType

        def update_data_type(self, data):
                self.dataType = data 

        def add_data(self,dataName,content):
                print(f"add data -> dataName = {dataName} , content = {content}")
                for field in self.fields:
                        if transform_name(dataName)== field.get_name():
                               field.add_data(content)

        def get_data(self,dataName,contextFunc):

                for field in self.fields:
                        if dataName == field.get_name():
                                print()
                                return field.get_data()       

                for field in self.fields:
                        if field.typ in contextFunc:
                                result = contextFunc[field.typ].get_data(dataName,contextFunc)
                                if type(result) != str:
                                        return result
                return ""
        def get_datas(self,contextFunc):
                result = []
                for field in self.fields:
                        print(f"field name = {field.get_name()}")
                        if not isinstance(field.get_data(),str):
                                result.append((field.get_name(),field.get_data()))
                        if field.typ in contextFunc:
                                data = contextFunc[field.typ].get_datas(contextFunc)
                                print(f"field_type = {field.typ}, data = {data}")
                                result += data
                return result



        def get_var_names(self,contextFunc):
                result = []
                for field in self.fields:
                        if field.typ in contextFunc:
                                fieldResult = contextFunc[field.typ].get_var_names(contextFunc)
                                for res in fieldResult:
                                        result.append(field.name + "." +res)
                        else:
                                result.append(field.name)
                return result
        

        def add_datatype_name(self,name):
                self.datatype_name = name
                self.is_datatype = True

        def get_annotations(self):
                return self.annotations

        def get_var(self,name,contextFun):
                if name.__contains__("."):
                        nameSplit = name.split(".")
                        result = z3.Const(nameSplit[0],self.get_data_type()) 

                        for n in nameSplit[1:]:
                                getData =  self.get_data(transform_name(n),contextFun)
                                if type(getData) == str:
                                        raise ValueError(
                                                "{} is not defined as variable in the context.".format(n)) 
                                else:
                                        result = getData(result)
                return result

        def get_fields(self):
                return self.fields

        def get_func(self):

                return self.func

                
        def add_conditions(self, inputCond, funContext):
                print(f"inputCond = {inputCond}")
                self.save_inputCond = inputCond
                self.func = VFunction(
                        outputs = [self.get_data_type()],
                        inputs = [],
                        pre_condition = [lambda ins: True],
                        post_condition = [lambda ins, outs: self.post_conds_create(outs,inputCond,funContext,"create")],
                )
                

        def maintain_data(self,var,funcContext):

                keep_data = VFunction(
                        outputs = [self.get_data_type()],
                        inputs = [self.get_data_type()],
                        pre_condition = [lambda ins: True],
                        post_condition = [lambda ins, outs: self.create_keep_cond(ins,outs,var,funcContext)],
                )

                return keep_data


        def get_datatypes_fields(self,funcContext):
                data = []
                fieldContext = None
                for field in self.fields:
                        if field.typ != fieldContext and not field.get_typ() in base_types:
                                fieldContext = funcContext[field.get_typ()]
                                data = fieldContext.get_datatypes_fields(funcContext)
                newData = []
                for d in data:
                        for field in self.fields:
                                name, func = d
                                name = field.get_name() +"."+ name
                                func = [field.get_data()] + func
                                newData.append((name,func))
                if len(data) == 0:
                        for field in self.fields:
                                name = field.get_name()
                                func = [field.get_data()]
                                newData.append((name,func))

                return newData
                 
        def is_data(self,data):
                data = transform_name(data)
                if "." in data:
                        splitData = data.split(".")
                        firstPart = splitData[0]
                        data = firstPart
                        print(f"data = {data}")

                for field in self.fields:
                        print(f"field name = {field.name} data = {data}")
                        if data == field.name:
                                return True

                return False


        def keep_done_conds(self,funcContext):
                conds = self.save_inputCond
                keep_conds = VFunction(
                        outputs = [self.get_data_type()],
                        inputs = [self.get_data_type()],
                        pre_condition = [lambda ins: True],
                        post_condition = [lambda ins, outs: self.post_conds_create(outs,conds,funcContext,"condition")],
                )

                return keep_conds                

        def create_keep_cond(self,ins,outs,var,funcContext):
                varSplit = var.split(".")
                newVar = ""
                for varS in varSplit[1:]:
                        newVar += varS + "."
                result = []
                newVar = newVar[:-1]
                data = self.get_datatypes_fields(funcContext)
                for d in data:
                        name, func = d

                        if name != newVar:
                                finalFuncOuts = outs
                                finalFuncIns = ins
                                for funDt in func:       
                                        finalFuncOuts = funDt(finalFuncOuts)
                                        finalFuncIns = funDt(finalFuncIns)   
                                result.append(var_unit(finalFuncOuts) == var_unit(finalFuncIns))
                                result.append(var_value(finalFuncOuts) == var_value(finalFuncIns))
                
                print(f"result create_keep_cond = {result}")
                
                return z3.And(*result)
                        




        def post_conds_create(self,outs,inputCond,funContext,mode):
                result = []
                #print(f"inputCond = {inputCond} in post_conds_create")
                for cond in inputCond:
                        cond , typeCond = self.create_line_cond(outs,cond,funContext,mode)
                        print(f"cond = {cond} , type = {type(cond)}")
                        if cond is not None and typeCond == mode:
                                result.append(cond)
                print(f"result = {result}")
                if len(result) == 1:
                        return result[0]
                else:
                        return z3.And(*result)

        def create_line_cond(self,outs,InputCond,funContext, mode):
                if isinstance(InputCond,LogicalExpression):
                        print(f"test operator = {InputCond.get_operador()}")
                        leftside = InputCond.get_left_side()
                        rightside = InputCond.get_right_side()
                        print(f"input cond left side type = {type(InputCond.get_left_side())}")
                        print(f"input cond right side type = {type(InputCond.get_right_side())}")
                        leftsideCond , leftType =self.create_line_cond(outs,InputCond.get_left_side(),funContext,mode)
                        rightsideCond , rightType =self.create_line_cond(outs,InputCond.get_right_side(),funContext,mode)
                        print(f"left side = {leftsideCond} type = {type(leftsideCond)}")
                        print(f"righ side = {rightsideCond} type = {type(rightsideCond)}")
                        if InputCond.get_operador() == "and":
                                if rightType == mode and leftType == mode:
                                        return z3.And(leftsideCond,rightsideCond), mode
                                elif rightType == mode:
                                        return rightsideCond , mode
                                elif leftType == mode:
                                        return leftsideCond , mode
                        elif InputCond.get_operador() == "or":
                                #Always condition
                                print("ENTREI NO OR ")
                                return z3.Or(leftsideCond,rightsideCond) , "condition"
                        
                elif isinstance(InputCond,IfExpression):
                        truePart , = self.create_line_cond(outs,InputCond.get_true_part(),funContext,mode)
                        falsePart , = self.create_line_cond(outs,InputCond.get_false_part(),funContext,mode)
                        return z3.Or(truePart,falsePart) , "condition"
                elif isinstance(InputCond,FunctionExpression):
                        if InputCond.get_name() == "Unit":
                                var =  InputCond.get_args()[0].__str__()
                                unit = InputCond.get_left_side().__str__()

                                if unit[0] == '"':
                                        unit = unit[1:]

                                if unit[-1] == '"':
                                        unit = unit[:-1]

                                varResult = outs
                                if var.__contains__("."):
                                        varSplit = var.split(".")
                                        for varS in varSplit:
                                                varResult = self.get_data(transform_name(varS),funContext)(varResult)
                                else:
                                        varResult = self.get_data(transform_name(var),funContext)(varResult)
                                unitz3 = z3.StringVal(unit)
                                result : z3.ExprRef = var_unit(varResult) == unitz3
                                return result , "create"
                elif isinstance(InputCond,Condition):
                          #TODO
                        print(f"annotation appended in Context {InputCond.__str__()}")  	                  
                        #self.annotations.append(InputCond.__str__())
                        left  = InputCond.get_left_side().__str__()
                        right = InputCond.get_right_side().__str__()
                        varResult = outs
                        print(f"funContext = {funContext}")
                        if self.is_data(left):
                                if left.__contains__("."):
                                        varSplit = left.split(".")
                                        for varS in varSplit:
                                                varResult = self.get_data(transform_name(varS),funContext)(varResult)
                                elif self.is_data(left):
                                        varResult = self.get_data(transform_name(left),funContext)(varResult)
                                left = varResult
                        else:
                                left = float(left)
                        varResult = outs
                        if self.is_data(right):
                                if right.__contains__("."):
                                        varSplit = right.split(".")
                                        for varS in varSplit:
                                                varResult = self.get_data(transform_name(varS),funContext)(varResult)
                                else:
                                        varResult = self.get_data(transform_name(right),funContext)(varResult)
                                right = varResult
                        else:
                                right = float(right)

                        op = InputCond.get_operador()
                        print(f"left = {left}")
                        print(f"op = {op}")
                        print(f"right = {right}, type = {type(right)}")
                        if op == "==":
                                if isinstance(right,float):
                                        result : z3.ExprRef = var_value(left) == right
                                        print(f"result = {result}")
                                        return result , "condition"
                                elif isinstance(left,float):
                                        result : z3.ExprRef = var_value(right) == left
                                        return result , "condition"
                                else:
                                        result : z3.ExprRef = var_value(left) == var_value(right)
                                        return result , "condition"
                        elif op == ">":
                                if isinstance(right,float):
                                        result : z3.ExprRef = var_value(left) > right
                                        return result , "condition"
                                elif isinstance(left,float):
                                        result : z3.ExprRef = var_value(right) > left
                                        return result , "condition"
                                else:
                                        result : z3.ExprRef = var_value(left) > var_value(right)
                                        return result , "condition"
                        elif op == ">=":
                                if isinstance(right,float):
                                        result : z3.ExprRef = var_value(left) >= right
                                        return result , "condition"
                                elif isinstance(left,float):
                                        result : z3.ExprRef = var_value(right) >= left
                                        return result , "condition"
                                else:
                                        result : z3.ExprRef = var_value(left) >= var_value(right)
                                        return result , "condition"
                        elif op == "<":
                                if isinstance(right,float):
                                        result : z3.ExprRef = var_value(left) < right
                                        return result , "condition"
                                elif isinstance(left,float):
                                        result : z3.ExprRef = var_value(right) < left
                                        return result , "condition"
                                else:
                                        result : z3.ExprRef = var_value(left) < var_value(right)
                                        return result , "condition"
                        elif op == "<=":
                                if isinstance(right,float):
                                        result : z3.ExprRef = var_value(left) <= right
                                        return result , "condition"
                                elif isinstance(left,float):
                                        result : z3.ExprRef = var_value(right) <= left
                                        return result , "condition"
                                else:
                                        result : z3.ExprRef = var_value(left) <= var_value(right)
                                        return result , "condition"
                        elif op == "!=":
                                if isinstance(right,float):
                                        result : z3.ExprRef = var_value(left) != right
                                        return result , "condition"
                                elif isinstance(left,float):
                                        result : z3.ExprRef = var_value(right) != left
                                        return result , "condition"
                                else:
                                        result : z3.ExprRef = var_value(left) != var_value(right)
                                        return result , "condition"
                        return True , "create"     
                return "None","None"                

