import types
import typing

import genpy

class GetJointPropertiesRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    joint_name: str

    def __init__(self, joint_name: str = ..., *args: typing.Any, **kwds: typing.Any) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetJointPropertiesRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetJointPropertiesRequest: ...

class GetJointPropertiesResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    REVOLUTE: int
    CONTINUOUS: int
    PRISMATIC: int
    FIXED: int
    BALL: int
    UNIVERSAL: int

    # Fields
    type: int
    damping: typing.List[float]
    position: typing.List[float]
    rate: typing.List[float]
    success: bool
    status_message: str

    def __init__(
        self,
        type: int = ...,
        damping: typing.List[float] = ...,
        position: typing.List[float] = ...,
        rate: typing.List[float] = ...,
        success: bool = ...,
        status_message: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetJointPropertiesResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetJointPropertiesResponse: ...

class GetJointProperties(object):
    _type: str
    _md5sum: str
    _request_class = GetJointPropertiesRequest
    _response_class = GetJointPropertiesResponse
