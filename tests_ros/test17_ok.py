#! /usr/bin/env python

from typing_extensions import Annotated


x : Annotated[int,""]

timestamp : Annotated[int, "_ < 10"]

x = 5

timestamp = x