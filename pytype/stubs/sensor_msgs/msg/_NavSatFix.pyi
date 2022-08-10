import types
import typing

import genpy
import sensor_msgs.msg
import std_msgs.msg

class NavSatFix(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    COVARIANCE_TYPE_UNKNOWN: int
    COVARIANCE_TYPE_APPROXIMATED: int
    COVARIANCE_TYPE_DIAGONAL_KNOWN: int
    COVARIANCE_TYPE_KNOWN: int

    # Fields
    header: std_msgs.msg.Header
    status: sensor_msgs.msg.NavSatStatus
    latitude: float
    longitude: float
    altitude: float
    position_covariance: typing.List[float]
    position_covariance_type: int

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        status: sensor_msgs.msg.NavSatStatus = ...,
        latitude: float = ...,
        longitude: float = ...,
        altitude: float = ...,
        position_covariance: typing.List[float] = ...,
        position_covariance_type: int = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> NavSatFix: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> NavSatFix: ...
