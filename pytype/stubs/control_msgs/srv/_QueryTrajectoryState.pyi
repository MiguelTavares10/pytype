import types
import typing

import genpy

class QueryTrajectoryStateRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    time: genpy.Time

    def __init__(self, time: genpy.Time = ..., *args: typing.Any, **kwds: typing.Any) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> QueryTrajectoryStateRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> QueryTrajectoryStateRequest: ...

class QueryTrajectoryStateResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    name: typing.List[str]
    position: typing.List[float]
    velocity: typing.List[float]
    acceleration: typing.List[float]

    def __init__(
        self,
        name: typing.List[str] = ...,
        position: typing.List[float] = ...,
        velocity: typing.List[float] = ...,
        acceleration: typing.List[float] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> QueryTrajectoryStateResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> QueryTrajectoryStateResponse: ...

class QueryTrajectoryState(object):
    _type: str
    _md5sum: str
    _request_class = QueryTrajectoryStateRequest
    _response_class = QueryTrajectoryStateResponse
