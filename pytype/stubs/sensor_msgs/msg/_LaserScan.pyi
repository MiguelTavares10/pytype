import types
import typing

import genpy
import std_msgs.msg

class LaserScan(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    angle_min: float
    angle_max: float
    angle_increment: float
    time_increment: float
    scan_time: float
    range_min: float
    range_max: float
    ranges: typing.List[float]
    intensities: typing.List[float]

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        angle_min: float = ...,
        angle_max: float = ...,
        angle_increment: float = ...,
        time_increment: float = ...,
        scan_time: float = ...,
        range_min: float = ...,
        range_max: float = ...,
        ranges: typing.List[float] = ...,
        intensities: typing.List[float] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> LaserScan: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> LaserScan: ...
