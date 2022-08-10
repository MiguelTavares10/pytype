from typing_extensions import Annotated

variableFrame : Annotated[int,"Unit('NED')"]
x : Annotated[int,"Unit('ENU')"]
x = 1
send_attitude_target = x