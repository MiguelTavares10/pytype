import types
import typing

import genpy
import sensor_msgs.msg

class GetPointMapROIRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    x: float
    y: float
    z: float
    r: float
    l_x: float
    l_y: float
    l_z: float

    def __init__(
        self,
        x: float = ...,
        y: float = ...,
        z: float = ...,
        r: float = ...,
        l_x: float = ...,
        l_y: float = ...,
        l_z: float = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetPointMapROIRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetPointMapROIRequest: ...

class GetPointMapROIResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    sub_map: sensor_msgs.msg.PointCloud2

    def __init__(
        self,
        sub_map: sensor_msgs.msg.PointCloud2 = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetPointMapROIResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetPointMapROIResponse: ...

class GetPointMapROI(object):
    _type: str
    _md5sum: str
    _request_class = GetPointMapROIRequest
    _response_class = GetPointMapROIResponse
