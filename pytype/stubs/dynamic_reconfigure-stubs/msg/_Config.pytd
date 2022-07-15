import types
import typing

import dynamic_reconfigure.msg
import genpy

class Config(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    bools: typing.List[dynamic_reconfigure.msg.BoolParameter]
    ints: typing.List[dynamic_reconfigure.msg.IntParameter]
    strs: typing.List[dynamic_reconfigure.msg.StrParameter]
    doubles: typing.List[dynamic_reconfigure.msg.DoubleParameter]
    groups: typing.List[dynamic_reconfigure.msg.GroupState]

    def __init__(
        self,
        bools: typing.List[dynamic_reconfigure.msg.BoolParameter] = ...,
        ints: typing.List[dynamic_reconfigure.msg.IntParameter] = ...,
        strs: typing.List[dynamic_reconfigure.msg.StrParameter] = ...,
        doubles: typing.List[dynamic_reconfigure.msg.DoubleParameter] = ...,
        groups: typing.List[dynamic_reconfigure.msg.GroupState] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> Config: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> Config: ...
