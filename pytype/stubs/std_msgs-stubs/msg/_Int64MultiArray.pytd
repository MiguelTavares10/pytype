import types
import typing

import genpy
import std_msgs.msg

class Int64MultiArray(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    layout: std_msgs.msg.MultiArrayLayout
    data: typing.List[int]

    def __init__(
        self,
        layout: std_msgs.msg.MultiArrayLayout = ...,
        data: typing.List[int] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> Int64MultiArray: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> Int64MultiArray: ...
