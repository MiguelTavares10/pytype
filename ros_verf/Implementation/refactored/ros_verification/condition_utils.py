

from ros_verf.Implementation.refactored.ros_verification.context_vars import GlobalContext, InstanceContext


def add_context_names_to_condition(cond :str, context:dict):
    cond = cond + " "
    condSplitted = cond.split(" ")
    newCond = ""
    for data in condSplitted:
        if data in context:
            if isinstance(context[data],GlobalContext):
                globalContext : GlobalContext = context[data]
                lastIns : InstanceContext = globalContext.get_last_instance()
                newCond += " " + lastIns.get_name() + " "
        elif data.__contains__("."):
            dataSplit= data.split(".")
            if dataSplit[0] in context:
                if isinstance(context[dataSplit[0]],GlobalContext):
                    classContext : GlobalContext = context[dataSplit[0]]
                    lastClassInst : InstanceContext = classContext.get_last_instance()
                    classPart = lastClassInst.get_name()
                    for stringData in dataSplit[1:]:
                        if stringData == "x":
                            classPart = "vectorX(" + classPart + ")"
                        elif stringData == "y":
                            classPart = "vectorY(" + classPart + ")"
                        elif stringData == "z":
                            classPart = "vectorZ(" + classPart + ")"
                        else:
                            classPart = stringData + "(" + classPart + ")"  

                    newCond += " " + classPart  + " "
                else:
                    newCond += data
            else:
                newCond += data
        else:     
            newCond += data

    return newCond
