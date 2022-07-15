import types
import typing

import genpy
import sensor_msgs.msg
import std_msgs.msg

class CameraInfo(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    height: int
    width: int
    distortion_model: str
    D: typing.List[float]
    K: typing.List[float]
    R: typing.List[float]
    P: typing.List[float]
    binning_x: int
    binning_y: int
    roi: sensor_msgs.msg.RegionOfInterest

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        height: int = ...,
        width: int = ...,
        distortion_model: str = ...,
        D: typing.List[float] = ...,
        K: typing.List[float] = ...,
        R: typing.List[float] = ...,
        P: typing.List[float] = ...,
        binning_x: int = ...,
        binning_y: int = ...,
        roi: sensor_msgs.msg.RegionOfInterest = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> CameraInfo: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> CameraInfo: ...
