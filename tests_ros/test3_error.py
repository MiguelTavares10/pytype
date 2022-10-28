#! /usr/bin/env python
from typing_extensions import Annotated



z : Annotated[float, "Unit('quaternion')"]
z = 6
a : Annotated[float, "Unit('meter')"]
b : Annotated[float, "Unit('quaternion')"]
a = 10
b = 20
z = b
a = z

