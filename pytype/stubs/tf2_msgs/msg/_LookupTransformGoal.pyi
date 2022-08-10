import types
import typing

import genpy

class LookupTransformGoal(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    target_frame: str
    source_frame: str
    source_time: genpy.Time
    timeout: genpy.Duration
    target_time: genpy.Time
    fixed_frame: str
    advanced: bool

    def __init__(
        self,
        target_frame: str = ...,
        source_frame: str = ...,
        source_time: genpy.Time = ...,
        timeout: genpy.Duration = ...,
        target_time: genpy.Time = ...,
        fixed_frame: str = ...,
        advanced: bool = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> LookupTransformGoal: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> LookupTransformGoal: ...
