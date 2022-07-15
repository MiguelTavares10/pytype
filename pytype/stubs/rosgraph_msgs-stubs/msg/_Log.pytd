import types
import typing

import genpy
import std_msgs.msg

class Log(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    DEBUG: byte
    INFO: byte
    WARN: byte
    ERROR: byte
    FATAL: byte

    # Fields
    header: std_msgs.msg.Header
    level: byte
    name: str
    msg: str
    file: str
    function: str
    line: int
    topics: typing.List[str]

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        level: byte = ...,
        name: str = ...,
        msg: str = ...,
        file: str = ...,
        function: str = ...,
        line: int = ...,
        topics: typing.List[str] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> Log: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> Log: ...
