import types
import typing

import dynamic_reconfigure.msg
import genpy

class Group(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    name: str
    type: str
    parameters: typing.List[dynamic_reconfigure.msg.ParamDescription]
    parent: int
    id: int

    def __init__(
        self,
        name: str = ...,
        type: str = ...,
        parameters: typing.List[dynamic_reconfigure.msg.ParamDescription] = ...,
        parent: int = ...,
        id: int = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> Group: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> Group: ...
