import types
import typing

import genpy
import geometry_msgs.msg
import std_msgs.msg

class GetModelStateRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    model_name: str
    relative_entity_name: str

    def __init__(
        self,
        model_name: str = ...,
        relative_entity_name: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetModelStateRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetModelStateRequest: ...

class GetModelStateResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    pose: geometry_msgs.msg.Pose
    twist: geometry_msgs.msg.Twist
    success: bool
    status_message: str

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        pose: geometry_msgs.msg.Pose = ...,
        twist: geometry_msgs.msg.Twist = ...,
        success: bool = ...,
        status_message: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetModelStateResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetModelStateResponse: ...

class GetModelState(object):
    _type: str
    _md5sum: str
    _request_class = GetModelStateRequest
    _response_class = GetModelStateResponse
