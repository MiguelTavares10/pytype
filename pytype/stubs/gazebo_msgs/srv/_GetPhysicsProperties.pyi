import types
import typing

import gazebo_msgs.msg
import genpy
import geometry_msgs.msg

class GetPhysicsPropertiesRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    def __init__(self, *args: typing.Any, **kwds: typing.Any) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetPhysicsPropertiesRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetPhysicsPropertiesRequest: ...

class GetPhysicsPropertiesResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    time_step: float
    pause: bool
    max_update_rate: float
    gravity: geometry_msgs.msg.Vector3
    ode_config: gazebo_msgs.msg.ODEPhysics
    success: bool
    status_message: str

    def __init__(
        self,
        time_step: float = ...,
        pause: bool = ...,
        max_update_rate: float = ...,
        gravity: geometry_msgs.msg.Vector3 = ...,
        ode_config: gazebo_msgs.msg.ODEPhysics = ...,
        success: bool = ...,
        status_message: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetPhysicsPropertiesResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetPhysicsPropertiesResponse: ...

class GetPhysicsProperties(object):
    _type: str
    _md5sum: str
    _request_class = GetPhysicsPropertiesRequest
    _response_class = GetPhysicsPropertiesResponse
