
from typing import Union
from z3 import *
from ros_verf.Implementation.refactored.ros_verification.dsl import VFunction,  StrLit, Code , Line
from ros_verf.Implementation.refactored.ros_verification.context_vars import GlobalContext, InstanceContext
from ros_verf.Implementation.refactored.ros_verification.condition_utils import add_context_names_to_condition
from ros_verf.Implementation.refactored.ros_verification.context_func import FuncContext
from ros_verf.Implementation.refactored.ros_verification.prelude import TVar, var_unit, var_value
from ros_verf.Implementation.refactored.ros_verification.run_prelude import run_prelude
from ros_verf.Implementation.refactored.ros_verification.AnnotatedHandler import AnnotatedHandler

COMMAND_LINE_BRACKETS = "###################################################################################"
KEY_NEW_VAR = "_"
def build_initial_context():
    context = {}

    context["default"] = VFunction(
        outputs = [],
        inputs = [],
        pre_condition = [lambda ins: True],
        post_condition = [lambda ins, outs: True],
    )

    context["create_unit"] = VFunction(
        outputs=[TVar],
        inputs=[StrLit],
        pre_condition=[lambda ins: True],
        post_condition=[lambda ins, outs: var_unit(outs[0]) == ins[0]],
    )

    context["add_unit"] = VFunction(
        outputs = [TVar],
        inputs = [TVar,StrLit],
        pre_condition = [lambda ins: True], # lambda ins: var_unit(ins[0]) == "None"
        post_condition = [lambda ins, outs: z3.And(var_unit(outs[0]) == ins[1],var_value(outs[0]) == var_value(ins[0]))],
    )
    #vectorX(linear(move)
    context["add_value"] = VFunction(
        outputs = [TVar],
        inputs = [TVar, z3.Reals],
        pre_condition = [lambda ins: True],
        post_condition = [lambda ins, outs: z3.And(var_value(outs[0]) == ins[1],var_unit(outs[0]) == var_unit(ins[0]))],
    )

    context["assign"] = VFunction(
        outputs=[TVar],
        inputs=[TVar,TVar],
        pre_condition=[lambda ins: var_unit(ins[0]) == var_unit(ins[1])], 
        post_condition=[lambda ins, outs: z3.And(var_unit(outs[0]) == var_unit(ins[0]),
                                                var_unit(outs[0]) == var_unit(ins[1]),
                                                var_value(outs[0]) == var_value(ins[1]))],
    )


    context["plus_vars"] = VFunction(
        outputs = [TVar],
        inputs = [TVar,TVar,TVar],
        pre_condition = [lambda ins: z3.And(var_unit(ins[0]) == var_unit(ins[1]),
                                            var_unit(ins[0]) == var_unit(ins[2]))],
        post_condition = [lambda ins, outs: z3.And(var_unit(outs[0]) == var_unit(ins[0]),
                                                    var_unit(outs[0]) == var_unit(ins[1]),
                                                    var_unit(outs[0]) == var_unit(ins[2]),
                                                    var_value(outs[0]) == (var_value(ins[1]) + var_value(ins[2])))],
    )


    context["plus_cons"] = VFunction(
    outputs = [TVar],
    inputs = [TVar,TVar,z3.Reals],
    pre_condition = [lambda ins: var_unit(ins[0]) == var_unit(ins[1])],
    post_condition = [lambda ins, outs: z3.And(var_unit(outs[0]) == var_unit(ins[0]),
                                                var_unit(outs[0]) == var_unit(ins[1]),
                                                var_value(outs[0]) == (var_value(ins[1]) + ins[2]))],
    )


    context["minus_vars"] = VFunction(
        outputs = [TVar],
        inputs = [TVar,TVar,TVar],
        pre_condition = [lambda ins: z3.And(var_unit(ins[0]) == var_unit(ins[1]),
                                            var_unit(ins[0]) == var_unit(ins[2]))],
        post_condition = [lambda ins, outs: z3.And(var_unit(outs[0]) == var_unit(ins[0]),
                                                    var_unit(outs[0]) == var_unit(ins[1]),
                                                    var_unit(outs[0]) == var_unit(ins[2]),
                                                    var_value(outs[0]) == (var_value(ins[1]) - var_value(ins[2])))],
    )


    context["minus_var_cons"] = VFunction(
    outputs = [TVar],
    inputs = [TVar,TVar,z3.Reals],
    pre_condition = [lambda ins: var_unit(ins[0]) == var_unit(ins[1])],
    post_condition = [lambda ins, outs: z3.And(var_unit(outs[0]) == var_unit(ins[0]),
                                                var_unit(outs[0]) == var_unit(ins[1]),
                                                var_value(outs[0]) == (var_value(ins[1]) - ins[2]))],
    )

    context["minus_cons_var"] = VFunction(
    outputs = [TVar],
    inputs = [TVar,z3.Reals, TVar],
    pre_condition = [lambda ins: var_unit(ins[0]) == var_unit(ins[2])],
    post_condition = [lambda ins, outs: z3.And(var_unit(outs[0]) == var_unit(ins[0]),
                                                var_unit(outs[0]) == var_unit(ins[2]),
                                                var_value(outs[0]) == (ins[1] - var_value(ins[2])))],
    )
    return context

def build_z3_object(o,func,datatype,funcContext):
    if func == "create_datatype":
        return z3.Const(o,funcContext[datatype].get_data_type())  
    elif isinstance(o,str):
        if o.__contains__('.'):
            dataSplited =o.split(".")
            locals()[dataSplited[0]] = z3.Const(dataSplited[0], funcContext[datatype].get_data_type())
            return funcContext[datatype].get_var(o,funcContext)
        return z3.Const((o),TVar)
    elif isinstance(o, StrLit):
        return z3.StringVal(o.s)
    else:
        return z3.RealVal(o)

def build_context_strings(objetos,func,context,output=False):
    newObjects = []
    for o in objetos:
        if isinstance(o,str):
            if o in context:
                if isinstance(context[o], GlobalContext):    
                    gblCtx : GlobalContext = context[o]
                    if output == True:
                        newObjects.append(gblCtx.add_instance())
                    else:
                        lastInts : InstanceContext = gblCtx.get_last_instance()
                        newObjects.append(lastInts.get_name())
            elif o.__contains__("."):
                oSplit= o.split(".")
                if oSplit[0] in context:
                    classContext : GlobalContext = context[oSplit[0]]
                    newObj = ""
                    if output:
                        newObj = classContext.add_instance()
                    else:
                        newClassIns = classContext.get_last_instance()
                        newObj = newClassIns.get_name()
                    for oS in oSplit[1:]:
                        newObj += "." + oS
                    
                    newObjects.append(newObj)
                                       
            else:
                if func == "create_datatype":
                    context[o]= GlobalContext(o)
                    newObjects.append(o)
                elif o.__contains__("."):
                    dataSplited = o.split(".")
                    name = dataSplited[0]
                    if name in context:
                        gblCtx : GlobalContext = context[dataSplited[0]]
                        instCtx : InstanceContext = gblCtx.get_last_instance()
                        o = instCtx.get_name()
                        for ds in dataSplited[1:]:
                            o += "." + ds

                else: 
                        raise ValueError(
                            "{} is not defined as variable in the context.".format(o)) 
        
        else:
            newObjects.append(o)

    return newObjects , context
                
def transform_name(name):
        if name == "x":
                return "vectorX"
        if name == "y":
                return "vectorY"
        if name == "z":
                return "vectorZ"
        return name

def verify_lines(line: Line, context: dict, funcContext , solver=None):
    (outputs, func, inputs) = line
    print(line)
    if solver == None:
        solver = z3.Solver            
    if func == "condition":
        if outputs[0] in context:
            if isinstance(context[outputs[0]],GlobalContext):
                glbctx : GlobalContext = context[outputs[0]]
                glbctx.add_global_data(inputs[0])
                print(f"inputs0 added {inputs[0]}")
            else:
                raise ValueError(
                    "{} is not defined as variable in the context.".format(outputs[0]))
        elif outputs[0].__contains__("."):
                dataSplitted = outputs[0].split(".")
                className = dataSplitted[0]
                if className in context:
                    classContext : GlobalContext= context[className]
                    classContext.add_global_data(inputs[0])
                else:
                    raise ValueError(
                        "{} is not defined in the context.".format(outputs[0]))
            
        else:
            context[outputs[0]] = GlobalContext(outputs[0],gblData=inputs[0])
        
        return context

    if func not in context and not func == "create_datatype":
        raise ValueError(
            "Function {} is not defined in the context.".format(func))

    if func == "create_datatype":
        dfun = funcContext[inputs[0]].get_func() 
        vars = funcContext[inputs[0]].get_datatypes_fields(funcContext)
        annotHandler = AnnotatedHandler.getInstance()
        for var in vars:
                annotatedVar = outputs[0]+"."+var[0]
                annotHandler.add_var_annotated(annotatedVar)
                print(f"var = {annotatedVar}")

        assert isinstance(dfun, VFunction)
    else:
        dfun = context[func]
        assert isinstance(dfun, VFunction)

        if len(inputs) != len(dfun.inputs):
            raise ValueError("Function {} expects {} inputs, but {} were provided.".format(
                func, len(dfun.inputs), len(inputs)))

        if len(outputs) != len(dfun.outputs):
            raise ValueError("Function {} expects {} outputs, but {} were provided.".format(
                func, len(dfun.outputs), len(outputs)))


    if func == "create_unit":
            context[outputs[0]] = GlobalContext(outputs[0])


    newInputs, context = build_context_strings(inputs,func,context)
    
    newOutputs, context = build_context_strings(outputs,func,context,True)

    if func == "create_datatype":
        context[outputs[0]].add_datatype(inputs[0])         
    
    outputVar = outputs[0]
    if outputVar.__contains__("."):
        outputSplitVar = outputVar.split(".")
        outputVar = outputSplitVar[0]
    datatypeOut = context[outputVar].get_datatype()
    
    if func == "assign":
        inputVar = inputs[1]
        if inputVar.__contains__("."):
            inputSplitVar = inputVar.split(".")
            inputVar = inputSplitVar[0]
        datatypeInp = context[inputVar].get_datatype()
        symbolic_inputs = [build_z3_object(newInputs[0],func,datatypeOut,funcContext)]
        symbolic_inputs.append(build_z3_object(newInputs[1],func,datatypeInp,funcContext))
    else: 
        symbolic_inputs = [build_z3_object(i,func,datatypeOut,funcContext) for i in newInputs]

    symbolic_outputs = [build_z3_object(i,func,datatypeOut,funcContext) for i in newOutputs]

    if func == "add_value" or func == "add_unit" or func == "assign" or func == "plus_vars" or func == "plus_cons" or func == "minus_vars" or func == "minus_var_cons" or func == "minus_cons_var":
        outputsDatatype = outputs[0]
        if outputsDatatype.__contains__("."):
            outputsSplit = outputsDatatype.split(".")
            outputsDatatype = outputsSplit[0]
        if outputsDatatype.__contains__(KEY_NEW_VAR):
            outputsSplit = outputsDatatype.split(KEY_NEW_VAR)
            outputsDatatype = outputsSplit[0]
        dt = context[outputsDatatype].get_datatype() 
        if dt != "None":
            inp = newInputs[0]
            print(f"inp = {inp}")
            maintain_func = funcContext[dt].maintain_data(outputs[0],funcContext)
            assert isinstance(maintain_func, VFunction)
            if inp.__contains__("."):
                inpS = inp.split(".")
                inp = inpS[0]
            sym_inp = z3.Const(inp,funcContext[dt].get_data_type()) 
            out = newOutputs[0]
            if out.__contains__("."):
                outS = out.split(".")
                out = outS[0]
            sym_out = z3.Const(out,funcContext[dt].get_data_type()) 
            for prop in maintain_func.post_condition:
                solver.push()
                propData: Union[bool,z3.ExprRef]= prop(sym_inp, sym_out)
                print(propData)
                solver.add(propData)


        

    for prop in dfun.pre_condition:


        propo : Union[bool,z3.ExprRef]= prop(symbolic_inputs)
        print(propo)
        solver.push()
        solver.add(z3.Not(propo))
    
        r = solver.check()
        if r == z3.sat:
            print("#################################################")
            print(solver)
            print("#################################################")
            raise ValueError("Precondition {} of {} is not satisfied. Example is: {}".format(prop, func, solver.model()))
        solver.pop()
            
  

    for prop in dfun.post_condition:
        solver.push()
        propData: Union[bool,z3.ExprRef]= prop(symbolic_inputs, symbolic_outputs)
        print(propData)
        print("##################################solver############################")
        print(solver)
        print("##################################solver############################")
        
        solver.add(propData)

    print(COMMAND_LINE_BRACKETS)
    if func == "add_value" or func == "add_unit" or func == "assign" or func == "plus_vars" or func == "plus_cons" or func == "minus_vars" or func == "minus_var_cons" or func == "minus_cons_var":
        if dt != "None":
            maintain_conds = funcContext[dt].keep_done_conds(funcContext)
            assert isinstance(maintain_conds, VFunction)
            for propCond in maintain_conds.post_condition:
                solver.push()
                propDataCond: Union[bool,z3.ExprRef]= propCond(sym_inp, sym_out)
                print("######################################")
                print(f"propDataCond = {propDataCond}")
                print("######################################")
                
                solver.add(z3.Not(propDataCond))
                r = solver.check()
                if r == z3.sat:
                    raise ValueError("Condition {} is not satisfied. Example is: {}".format(propDataCond,solver.model()))
                solver.pop()

    if func == "assign":
        inpDt = inputs[1]
        if inpDt.__contains__("."):
            inpsSplit = inpDt.split(".")
            inpDt = inpsSplit[0]
        if inpDt.__contains__(KEY_NEW_VAR):
            inpsSplit = inpDt.split(KEY_NEW_VAR)
            inpDt = inpsSplit[0]
        dt = context[inpDt].get_datatype() 
        
        if dt != "None":
            maintain_conds = funcContext[dt].keep_done_conds(funcContext)
            assert isinstance(maintain_conds, VFunction)
            for propCond in maintain_conds.post_condition:
                solver.push()
                inp = newInputs[1]
                print(f"inp = {inp}")
                maintain_func = funcContext[dt].maintain_data(outputs[0],funcContext)
                assert isinstance(maintain_func, VFunction)
                if inp.__contains__("."):
                    inpS = inp.split(".")
                    inp = inpS[0]
                sym_inp = z3.Const(inp,funcContext[dt].get_data_type()) 
                sym_out = sym_inp
                propDataCond: Union[bool,z3.ExprRef]= propCond(sym_inp, sym_out)
                print("######################################")
                print(f"propDataCond = {propDataCond}")
                print("######################################")
                
                solver.add(z3.Not(propDataCond))
                r = solver.check()
                if r == z3.sat:
                    raise ValueError("Condition {} is not satisfied. Example is: {}".format(propDataCond,solver.model()))
                solver.pop()

    if func == "create_datatype":
        condFuns = funcContext[inputs[0]].get_annotations()
        for condFun in condFuns:
            print(f"condFun before = {condFun}")
            for field in funcContext[inputs[0]].get_fields():
                print(f"running field {field.get_name()}")
                if not condFun.__contains__(outputs[0]) and condFun.__contains__(field.get_name()):
                    condFun = condFun.replace(field.get_name(),outputs[0]+"."+field.get_name())
            print(f"cond {condFun} added to {outputs[0]} conds")
            context[outputs[0]].add_global_data(condFun)        
    print(COMMAND_LINE_BRACKETS)
    if func == "assign" or func == "add_value" or func == "plus_vars" or func == "plus_cons" or func == "minus_vars" or func == "minus_cons_var" or func == "minus_var_cons":
        solver.push()
        print(f"inputs0 = {inputs[0]}")
        print(f"inputs0 in context ? {inputs[0] in context}")
        if inputs[0] in context:
            gblCtx : GlobalContext = context[inputs[0]]
            globalCond = gblCtx.get_global_data()
            print(f"globalCond = {globalCond}")
        elif inputs[0].__contains__("."):
            inputSplit = inputs[0].split(".")
            if inputSplit[0] in context:
                classContext : GlobalContext = context[inputSplit[0]]
                globalCond = classContext.get_global_data()

        if func == "assign":
            if inputs[1] in context:
                gblCtx : GlobalContext = context[inputs[0]]
                globalCond = globalCond + gblCtx.get_global_data()
                print(f"globalCond = {globalCond}")
            elif inputs[1].__contains__("."):
                inputSplit = inputs[1].split(".")
                if inputSplit[0] in context:
                    classContext : GlobalContext = context[inputSplit[0]]
                    globalCond += classContext.get_global_data()
        print(f"globalCond = {globalCond}")
        for cond in globalCond:
            print(cond)
            cond = add_context_names_to_condition(cond,context)
            print(f"cond = {cond}")
            condsplit = cond.split(" ")
            for condPart in condsplit:
                if condPart in context:
                    print(f"transform 1 {transform_name(condPart)}")
                    locals()[transform_name(condPart)] = build_z3_object(transform_name(condPart),"")   
                elif condPart.__contains__("("):
                    condPart = condPart.replace(")","(")
                    condClass = condPart.split("(")
                    for condC in condClass:
                        condCsplit = condC.split(KEY_NEW_VAR)
                        if condCsplit[0] in context:
                            print(f"transform 2 {transform_name(condC)}")
                            datatypeCondc = context[condCsplit[0]].get_datatype()
                            locals()[transform_name(condC)] = build_z3_object(str(transform_name(condC)),"create_datatype",datatypeCondc,funcContext)
                            datatypeCondc = context[condCsplit[0]].get_datatype()
                            datasFunc = funcContext[datatypeCondc].get_datas(funcContext)
                            for dataFunc in datasFunc:
                                nameFunc, dataFun = dataFunc
                                print(f"Transform 4 : {nameFunc} , {dataFun} = {type(dataFun)}")
                                locals()[transform_name(nameFunc)] = dataFun

                elif condPart.__contains__(KEY_NEW_VAR):
                    dataSplitted = condPart.split(KEY_NEW_VAR)
                    if dataSplitted[0] in context:
                        print(f"transform 3 {condPart}")
                        locals()[condPart] = build_z3_object(condPart,"","",funcContext)
                        cond = cond.replace(condPart,"var_value( " + condPart + " )")

            print(cond, "added to solver")
            if "!=" in cond:
                cond = cond.replace("!=" ,"==")
                print(cond)
                solver.add(eval(cond))
            else:
                solver.add(z3.Not(eval(cond)))


            r = solver.check()
            if r == z3.sat:
                raise ValueError("Condition {} is not satisfied. Example is: {}".format(cond,solver.model()))
            solver.pop()

    
    globalCtx = "None"
    outputLastIns = "None"

    if outputs[0] in context:
        print("add stuff to context", func)
        if isinstance(context[outputs[0]], GlobalContext):
            globalCtx : GlobalContext = context[outputs[0]]
            outputLastIns : InstanceContext = globalCtx.get_last_instance()
    elif outputs[0].__contains__("."):
        outputSplit = outputs[0].split(".")
        if outputSplit[0] in context:
            if isinstance(context[outputSplit[0]],GlobalContext):
                globalCtx : GlobalContext = context[outputSplit[0]]
                outputLastIns : InstanceContext = globalCtx.get_last_instance()
        
    if isinstance(globalCtx, GlobalContext):
            if func == "assign":    
                if inputs[1] in context:
                    inputCtx : GlobalContext = context[inputs[1]]
                    if isinstance(inputCtx, GlobalContext) :
                        inputInstCtx : InstanceContext = inputCtx.get_last_instance()
                        outputLastIns.add_data(inputInstCtx.get_data(inputs[1]),outputs[0])
                elif inputs[1].__contains__("."):
                    input1splitted = inputs[1].split(".")
                    if input1splitted[0] in context:
                        classContext : GlobalContext = context[input1splitted[0]]
                        classInsContext : InstanceContext = classContext.get_last_instance()
                        data_input = classInsContext.get_data(inputs[1])
                        print(f"data_input = {data_input}")
                        outputLastIns.add_data(data_input,outputs[0])
            elif func == "add_value":
                outputLastIns.add_data(inputs[1],outputs[0])
            elif func == "add_unit" :
                globalCtx.add_global_unit(inputs[1].s,outputs[0])
            elif func == "create_unit":
                globalCtx.add_global_unit(inputs[0].s,outputs[0])
            elif not func == "create_dataset" and not func == "condition": 
                if inputs[0] in context:
                    inputCtx : GlobalContext = context[inputs[0]]
                    if isinstance(inputCtx, GlobalContext):
                        inputInstCtx : InstanceContext = inputCtx.get_last_instance()
                        outputLastIns.add_data(inputInstCtx.get_data(inputs[0]),outputs[0])
                    elif inputs[0].__contains__("."):
                        inputSplit = inputs[0].split(".")
                        if inputSplit[0] in context:
                            classContext : GlobalContext = context[inputSplit[0]]
                            classInsContext : InstanceContext = classContext.get_last_instance()
                            outputLastIns.add_data(classInsContext.get_data(inputs[0]),outputs[0])
                else:
                    globalCtx.add_instance(inputs[1])

    return context , funcContext



def verify_code(code: Code, funcContext, advanced_properties=True):
    context = build_initial_context()
    solver = z3.Solver() if advanced_properties else None
    for line in code:
        verify_lines(line, context, funcContext , solver=solver)
