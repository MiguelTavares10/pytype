#! /usr/bin/env python

from re import A
from typing_extensions import Annotated



x : Annotated[float, "Unit('m/s')"]
z : Annotated[float, "Unit('rad/s')"]
x = 5
z = 6
a : Annotated[float, "Unit('m/s')"]
b : Annotated[float, "Unit('rad/s')"]
a = 10
b = 20
x = a
z = b
