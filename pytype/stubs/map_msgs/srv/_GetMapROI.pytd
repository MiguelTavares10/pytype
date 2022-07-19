import types
import typing

import genpy
import nav_msgs.msg

class GetMapROIRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    x: float
    y: float
    l_x: float
    l_y: float

    def __init__(
        self,
        x: float = ...,
        y: float = ...,
        l_x: float = ...,
        l_y: float = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetMapROIRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetMapROIRequest: ...

class GetMapROIResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    sub_map: nav_msgs.msg.OccupancyGrid

    def __init__(
        self,
        sub_map: nav_msgs.msg.OccupancyGrid = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetMapROIResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetMapROIResponse: ...

class GetMapROI(object):
    _type: str
    _md5sum: str
    _request_class = GetMapROIRequest
    _response_class = GetMapROIResponse
