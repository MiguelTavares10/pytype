import types
import typing

import genpy

class ProjectedMapInfo(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    frame_id: str
    x: float
    y: float
    width: float
    height: float
    min_z: float
    max_z: float

    def __init__(
        self,
        frame_id: str = ...,
        x: float = ...,
        y: float = ...,
        width: float = ...,
        height: float = ...,
        min_z: float = ...,
        max_z: float = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> ProjectedMapInfo: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> ProjectedMapInfo: ...
