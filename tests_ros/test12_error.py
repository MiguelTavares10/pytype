from typing_extensions import Annotated

variableFrame : Annotated[int,"Unit('ENU')"]
x : Annotated[int,"Unit('NED')"]
x = 1
send_attitude_target = x