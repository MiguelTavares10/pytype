import types
import typing

import genpy
import geometry_msgs.msg

class MapMetaData(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    map_load_time: genpy.Time
    resolution: float
    width: int
    height: int
    origin: geometry_msgs.msg.Pose

    def __init__(
        self,
        map_load_time: genpy.Time = ...,
        resolution: float = ...,
        width: int = ...,
        height: int = ...,
        origin: geometry_msgs.msg.Pose = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> MapMetaData: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> MapMetaData: ...
