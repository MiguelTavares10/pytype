import types
import typing

import genpy

class RegionOfInterest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    x_offset: int
    y_offset: int
    height: int
    width: int
    do_rectify: bool

    def __init__(
        self,
        x_offset: int = ...,
        y_offset: int = ...,
        height: int = ...,
        width: int = ...,
        do_rectify: bool = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> RegionOfInterest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> RegionOfInterest: ...
