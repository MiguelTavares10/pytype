import types
import typing

import genpy
import sensor_msgs.msg
import std_msgs.msg

class DisparityImage(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    image: sensor_msgs.msg.Image
    f: float
    T: float
    valid_window: sensor_msgs.msg.RegionOfInterest
    min_disparity: float
    max_disparity: float
    delta_d: float

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        image: sensor_msgs.msg.Image = ...,
        f: float = ...,
        T: float = ...,
        valid_window: sensor_msgs.msg.RegionOfInterest = ...,
        min_disparity: float = ...,
        max_disparity: float = ...,
        delta_d: float = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> DisparityImage: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> DisparityImage: ...
