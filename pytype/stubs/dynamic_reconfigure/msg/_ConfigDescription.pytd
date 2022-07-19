import types
import typing

import dynamic_reconfigure.msg
import genpy

class ConfigDescription(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    groups: typing.List[dynamic_reconfigure.msg.Group]
    max: dynamic_reconfigure.msg.Config
    min: dynamic_reconfigure.msg.Config
    dflt: dynamic_reconfigure.msg.Config

    def __init__(
        self,
        groups: typing.List[dynamic_reconfigure.msg.Group] = ...,
        max: dynamic_reconfigure.msg.Config = ...,
        min: dynamic_reconfigure.msg.Config = ...,
        dflt: dynamic_reconfigure.msg.Config = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> ConfigDescription: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> ConfigDescription: ...
