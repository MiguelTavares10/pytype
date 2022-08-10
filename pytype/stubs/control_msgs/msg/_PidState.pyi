import types
import typing

import genpy
import std_msgs.msg

class PidState(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    timestep: genpy.Duration
    error: float
    error_dot: float
    p_error: float
    i_error: float
    d_error: float
    p_term: float
    i_term: float
    d_term: float
    i_max: float
    i_min: float
    output: float

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        timestep: genpy.Duration = ...,
        error: float = ...,
        error_dot: float = ...,
        p_error: float = ...,
        i_error: float = ...,
        d_error: float = ...,
        p_term: float = ...,
        i_term: float = ...,
        d_term: float = ...,
        i_max: float = ...,
        i_min: float = ...,
        output: float = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> PidState: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> PidState: ...
