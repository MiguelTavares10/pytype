import types
import typing

import genpy

class PointField(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    INT8: int
    UINT8: int
    INT16: int
    UINT16: int
    INT32: int
    UINT32: int
    FLOAT32: int
    FLOAT64: int

    # Fields
    name: str
    offset: int
    datatype: int
    count: int

    def __init__(
        self,
        name: str = ...,
        offset: int = ...,
        datatype: int = ...,
        count: int = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> PointField: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> PointField: ...
