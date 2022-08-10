import types
import typing

import genpy
import geometry_msgs.msg
import nav_msgs.msg

class GetPlanRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    start: geometry_msgs.msg.PoseStamped
    goal: geometry_msgs.msg.PoseStamped
    tolerance: float

    def __init__(
        self,
        start: geometry_msgs.msg.PoseStamped = ...,
        goal: geometry_msgs.msg.PoseStamped = ...,
        tolerance: float = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetPlanRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetPlanRequest: ...

class GetPlanResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    plan: nav_msgs.msg.Path

    def __init__(self, plan: nav_msgs.msg.Path = ..., *args: typing.Any, **kwds: typing.Any) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetPlanResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetPlanResponse: ...

class GetPlan(object):
    _type: str
    _md5sum: str
    _request_class = GetPlanRequest
    _response_class = GetPlanResponse
