import types
import typing

import genpy
import std_msgs.msg

class JointControllerState(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    set_point: float
    process_value: float
    process_value_dot: float
    error: float
    time_step: float
    command: float
    p: float
    i: float
    d: float
    i_clamp: float
    antiwindup: bool

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        set_point: float = ...,
        process_value: float = ...,
        process_value_dot: float = ...,
        error: float = ...,
        time_step: float = ...,
        command: float = ...,
        p: float = ...,
        i: float = ...,
        d: float = ...,
        i_clamp: float = ...,
        antiwindup: bool = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> JointControllerState: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> JointControllerState: ...
