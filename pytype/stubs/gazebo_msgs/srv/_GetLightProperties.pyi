import types
import typing

import genpy
import std_msgs.msg

class GetLightPropertiesRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    light_name: str

    def __init__(self, light_name: str = ..., *args: typing.Any, **kwds: typing.Any) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetLightPropertiesRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetLightPropertiesRequest: ...

class GetLightPropertiesResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    diffuse: std_msgs.msg.ColorRGBA
    attenuation_constant: float
    attenuation_linear: float
    attenuation_quadratic: float
    success: bool
    status_message: str

    def __init__(
        self,
        diffuse: std_msgs.msg.ColorRGBA = ...,
        attenuation_constant: float = ...,
        attenuation_linear: float = ...,
        attenuation_quadratic: float = ...,
        success: bool = ...,
        status_message: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetLightPropertiesResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetLightPropertiesResponse: ...

class GetLightProperties(object):
    _type: str
    _md5sum: str
    _request_class = GetLightPropertiesRequest
    _response_class = GetLightPropertiesResponse
