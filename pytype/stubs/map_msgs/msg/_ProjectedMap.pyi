import types
import typing

import genpy
import nav_msgs.msg

class ProjectedMap(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    map: nav_msgs.msg.OccupancyGrid
    min_z: float
    max_z: float

    def __init__(
        self,
        map: nav_msgs.msg.OccupancyGrid = ...,
        min_z: float = ...,
        max_z: float = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> ProjectedMap: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> ProjectedMap: ...
