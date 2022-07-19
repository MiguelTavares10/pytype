import types
import typing

import genpy
import geometry_msgs.msg
import sensor_msgs.msg
import std_msgs.msg

class PointCloud(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    points: typing.List[geometry_msgs.msg.Point32]
    channels: typing.List[sensor_msgs.msg.ChannelFloat32]

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        points: typing.List[geometry_msgs.msg.Point32] = ...,
        channels: typing.List[sensor_msgs.msg.ChannelFloat32] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> PointCloud: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> PointCloud: ...
