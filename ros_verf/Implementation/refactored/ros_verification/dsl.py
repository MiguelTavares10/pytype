
from typing import Any, Callable, List, Tuple, Union
from dataclasses import dataclass

@dataclass
class StrLit(object):
    """ This string represents a string in the context of the DSL. """
    s : str

    

Line = Tuple[List[str], str , List[Union[str, StrLit,int,float]]]

Code = List[Line]



@dataclass
class VFunction(object):
    inputs: List[Any]
    outputs: List[Any]
    pre_condition: List[Callable[[List[Any]],Any]] # List of Z3 conditions
    post_condition: List[Callable[[List[Any], List[Any]],Any]] # List of Z3 conditions
