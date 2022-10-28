#! /usr/bin/env python
from typing_extensions import Annotated



x : Annotated[float, "Unit('meter')"]
z : Annotated[float, "Unit('quaternion')"]
x = 5
z = 6
a : Annotated[float, "Unit('meter')"]
b : Annotated[float, "Unit('quaternion')"]
a = 10
b = 20
x = a
z = b
