import types
import typing

import genpy
import std_msgs.msg

class Range(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    ULTRASOUND: int
    INFRARED: int

    # Fields
    header: std_msgs.msg.Header
    radiation_type: int
    field_of_view: float
    min_range: float
    max_range: float
    range: float

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        radiation_type: int = ...,
        field_of_view: float = ...,
        min_range: float = ...,
        max_range: float = ...,
        range: float = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> Range: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> Range: ...
