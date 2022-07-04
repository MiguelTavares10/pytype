from ros_verf.Implementation.refactored.ros_verification.context_func import FuncContext
from ros_verf.Implementation.refactored.ros_verification.parser.msg_ros import ROSMsgFormat, ROSField
from ros_verf.Implementation.refactored.ros_verification.parser.parser_msg import get_datatype
from ros_verf.Implementation.refactored.ros_verification.ROSMessagesAnnotated.parser import parse_comments, mk_parser
import z3
COMMAND_LINE_BRACKETS = "###################################################################################"
def transform_name(name):
        if name == "x":
                return "vectorX"
        if name == "y":
                return "vectorY"
        if name == "z":
                return "vectorZ"
        return name

def run_prelude():
        funcInput = "Twist"
        contextData = {}
        inputs = get_datatype(funcInput,[])
        print(COMMAND_LINE_BRACKETS)
        print("input Get Datatypes")
        print(inputs)
        print(COMMAND_LINE_BRACKETS)
        #[ROSMsgFormat(package='geometry_msgs', name='Vector3', definition='float64 x\nfloat64 y\nfloat64 z\n', fields=(ROSField(typ='float64', name='x', default_value=None), ROSField(typ='float64', name='y', default_value=None), ROSField(typ='float64', name='z', default_value=None)), constants=()), ROSMsgFormat(package='geometry_msgs', name='Twist', definition='Vector3  linear\nVector3  angular\n', fields=(ROSField(typ='geometry_msgs/Vector3', name='linear', default_value=None), ROSField(typ='geometry_msgs/Vector3', name='angular', default_value=None)), constants=())]

        for inp in inputs:
                contextData[inp.name] = FuncContext(inp.name,inp,contextData)
        # contextData["Vector3"] = FuncContext("Vector3",[('vectorX',float),('vectorY',float),('vectorZ',float)],contextData)
        # contextData["Twist"] = FuncContext("Twist",[("linear","Vector3"),("angular","Vector3")],contextData)

        datatypes = [value.get_data_type() for value in contextData.values()]

        datatypes = z3.CreateDatatypes(*datatypes)
        index = 0

        for value in contextData.values():
                value.update_data_type(datatypes[index])
                index += 1



        # Put this in fors later with strings from context and inputs
        for input in inputs:
                for ins in input.fields:
                        name = ins.name
                        contextData[input.name].add_data(name, getattr(contextData[input.name].get_data_type(),transform_name(name)))



        comments = parse_comments(input.name)
        parse = []
        for com in comments:
                parse.append(mk_parser().parse(com))
        contextData[input.name].add_conditions(parse,contextData)

        print(f"contextData conditions = {contextData[input.name].get_annotations()}")
        # comments = parser_comments(input.name)
        # print(COMMAND_LINE_BRACKETS)
        # print(f"Input Name {input.name}")
        # print(f"comments = {comments}")
        # print(COMMAND_LINE_BRACKETS)
        # contextData[input.name].add_conditions(comments)

        # Vector3 = z3.Datatype('Vector3')
        # Twist= z3.Datatype('Twist')

        # Vector3.declare('Vector',('vectorX',TVar),('vectorY',TVar),('vectorZ',TVar))

        # Twist.declare('Twist',('linear',Vector3),('angular',Vector3))

        # Twist, Vector3 = z3.CreateDatatypes(Twist, Vector3)

        # linear = Twist.linear

        # angular = Twist.angular

        # vectorX = Vector3.vectorX
        # vectorY = Vector3.vectorY
        # vectorZ = Vector3.vectorZ
        return contextData