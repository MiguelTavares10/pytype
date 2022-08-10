import types
import typing

import gazebo_msgs.msg
import genpy

class SetJointPropertiesRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    joint_name: str
    ode_joint_config: gazebo_msgs.msg.ODEJointProperties

    def __init__(
        self,
        joint_name: str = ...,
        ode_joint_config: gazebo_msgs.msg.ODEJointProperties = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> SetJointPropertiesRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SetJointPropertiesRequest: ...

class SetJointPropertiesResponse(genpy.Message):
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
    def deserialize(self, str: bytes) -> SetJointPropertiesResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SetJointPropertiesResponse: ...

class SetJointProperties(object):
    _type: str
    _md5sum: str
    _request_class = SetJointPropertiesRequest
    _response_class = SetJointPropertiesResponse
