import types
import typing

import genpy
import geometry_msgs.msg

class ApplyBodyWrenchRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    body_name: str
    reference_frame: str
    reference_point: geometry_msgs.msg.Point
    wrench: geometry_msgs.msg.Wrench
    start_time: genpy.Time
    duration: genpy.Duration

    def __init__(
        self,
        body_name: str = ...,
        reference_frame: str = ...,
        reference_point: geometry_msgs.msg.Point = ...,
        wrench: geometry_msgs.msg.Wrench = ...,
        start_time: genpy.Time = ...,
        duration: genpy.Duration = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> ApplyBodyWrenchRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> ApplyBodyWrenchRequest: ...

class ApplyBodyWrenchResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    success: bool
    status_message: str

    def __init__(
        self,
        success: bool = ...,
        status_message: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> ApplyBodyWrenchResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> ApplyBodyWrenchResponse: ...

class ApplyBodyWrench(object):
    _type: str
    _md5sum: str
    _request_class = ApplyBodyWrenchRequest
    _response_class = ApplyBodyWrenchResponse
