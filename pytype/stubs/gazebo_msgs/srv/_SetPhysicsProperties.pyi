import types
import typing

import gazebo_msgs.msg
import genpy
import geometry_msgs.msg

class SetPhysicsPropertiesRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    time_step: float
    max_update_rate: float
    gravity: geometry_msgs.msg.Vector3
    ode_config: gazebo_msgs.msg.ODEPhysics

    def __init__(
        self,
        time_step: float = ...,
        max_update_rate: float = ...,
        gravity: geometry_msgs.msg.Vector3 = ...,
        ode_config: gazebo_msgs.msg.ODEPhysics = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> SetPhysicsPropertiesRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SetPhysicsPropertiesRequest: ...

class SetPhysicsPropertiesResponse(genpy.Message):
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
    def deserialize(self, str: bytes) -> SetPhysicsPropertiesResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SetPhysicsPropertiesResponse: ...

class SetPhysicsProperties(object):
    _type: str
    _md5sum: str
    _request_class = SetPhysicsPropertiesRequest
    _response_class = SetPhysicsPropertiesResponse
