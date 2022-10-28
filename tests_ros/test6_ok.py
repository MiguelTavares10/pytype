#! /usr/bin/env python

from typing_extensions import Annotated


x : Annotated[float, " _ >= 3.141592653589793238 "]
x = 3.141592653589793238
