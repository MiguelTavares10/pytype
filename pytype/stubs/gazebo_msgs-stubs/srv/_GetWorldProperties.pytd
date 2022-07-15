import types
import typing

import genpy

class GetWorldPropertiesRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    def __init__(self, *args: typing.Any, **kwds: typing.Any) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetWorldPropertiesRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetWorldPropertiesRequest: ...

class GetWorldPropertiesResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    sim_time: float
    model_names: typing.List[str]
    rendering_enabled: bool
    success: bool
    status_message: str

    def __init__(
        self,
        sim_time: float = ...,
        model_names: typing.List[str] = ...,
        rendering_enabled: bool = ...,
        success: bool = ...,
        status_message: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetWorldPropertiesResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetWorldPropertiesResponse: ...

class GetWorldProperties(object):
    _type: str
    _md5sum: str
    _request_class = GetWorldPropertiesRequest
    _response_class = GetWorldPropertiesResponse
