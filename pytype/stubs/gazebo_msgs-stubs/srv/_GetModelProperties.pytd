import types
import typing

import genpy

class GetModelPropertiesRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    model_name: str

    def __init__(self, model_name: str = ..., *args: typing.Any, **kwds: typing.Any) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetModelPropertiesRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetModelPropertiesRequest: ...

class GetModelPropertiesResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    parent_model_name: str
    canonical_body_name: str
    body_names: typing.List[str]
    geom_names: typing.List[str]
    joint_names: typing.List[str]
    child_model_names: typing.List[str]
    is_static: bool
    success: bool
    status_message: str

    def __init__(
        self,
        parent_model_name: str = ...,
        canonical_body_name: str = ...,
        body_names: typing.List[str] = ...,
        geom_names: typing.List[str] = ...,
        joint_names: typing.List[str] = ...,
        child_model_names: typing.List[str] = ...,
        is_static: bool = ...,
        success: bool = ...,
        status_message: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetModelPropertiesResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetModelPropertiesResponse: ...

class GetModelProperties(object):
    _type: str
    _md5sum: str
    _request_class = GetModelPropertiesRequest
    _response_class = GetModelPropertiesResponse
