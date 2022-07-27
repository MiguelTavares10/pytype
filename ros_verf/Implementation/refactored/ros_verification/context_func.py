from z3 import *

from ros_verf.Implementation.refactored.ros_verification.prelude import TVar
from ros_verf.Implementation.refactored.ros_verification.dsl import VFunction 
from ros_verf.Implementation.refactored.ros_verification.prelude import var_unit, var_value, TVar
from ros_verf.Implementation.refactored.ros_verification.ParserMessages.ast_syntax import LogicalExpression, IfExpression, Condition, Literal, Variable,FunctionExpression, AritmeticExpression

COMMAND_LINE_BRACKETS = "###################################################################################"
base_types = ["float64","uint32","string"]
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
                self.dataType.declare(name,*newVars)       
                self.conds = []
                self.annotations = [] 
                self.func = "Nenhuma"
                self.keep_func = "Nenhuma"


        def get_name(self):
                return self.name


        def get_data_type(self):
                return self.dataType

        def update_data_type(self, data):
                self.dataType = data 

        def add_data(self,dataName,content):
                for field in self.fields:
                        if transform_name(dataName)== field.get_name():
                               field.add_data(content)

        def get_data(self,dataName,contextFunc):

                for field in self.fields:
                        if dataName == field.get_name():
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
                        if not isinstance(field.get_data(),str):
                                result.append((field.get_name(),field.get_data()))
                        if field.typ in contextFunc:
                                data = contextFunc[field.typ].get_datas(contextFunc)
                                result += data
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
                self.func = VFunction(
                        outputs = [self.get_data_type()],
                        inputs = [],
                        pre_condition = [lambda ins: True],
                        post_condition = [lambda ins, outs: self.post_conds_create(outs,inputCond,funContext)],
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
                        




        def post_conds_create(self,outs,inputCond,funContext):
                result = []
                #print(f"inputCond = {inputCond} in post_conds_create")
                for cond in inputCond:
                        cond = self.create_line_cond(outs,cond,funContext)
                        result.append(cond)

                return z3.And(*result)

        def create_line_cond(self,outs,InputCond,funContext):
                if isinstance(InputCond,LogicalExpression):

                        leftside =self.create_line_cond(outs,InputCond.get_left_side(),funContext)
                        rightside =self.create_line_cond(outs,InputCond.get_right_side(),funContext)

                        if InputCond.get_operador() == "and":
                                return z3.And(leftside,rightside)
                        elif InputCond.get_operador == "or":
                                return z3.Or(self.create_line_cond(outs,InputCond.get_left_side(),funContext),self.create_line_cond(outs,InputCond.get_right_side(),funContext))
                        
                elif isinstance(InputCond,IfExpression):
                        return z3.Or(self.create_line_cond(outs,InputCond.get_true_part(),funContext),self.create_line_cond(outs,InputCond.get_false_part(),funContext))
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
                                return result
                elif isinstance(InputCond,Condition):
                          #TODO
                        
                        print(f"annotation appended in Context {InputCond.__str__()}")  
                        stringInput = InputCond.__str__()
                        start = "var_value ( "
                        end = " )"
                        idx1 = stringInput.index(start)
                        idx2 = stringInput.index(end)
                        varResult = stringInput.index(end)
                        var = stringInput[idx1 + len(start): idx2]
                        varResult = outs
                        if var.__contains__("."):
                                varSplit = var.split(".")
                                for varS in varSplit:
                                        varResult = self.get_data(transform_name(varS),funContext)(varResult)
                        else:
                                varResult = self.get_data(transform_name(var),funContext)(varResult)
                        res = stringInput.replace(var,varResult.__str__())
                        print(f"res = {res}")
                        input()
                        self.annotations.append(res)
                        return True                      

