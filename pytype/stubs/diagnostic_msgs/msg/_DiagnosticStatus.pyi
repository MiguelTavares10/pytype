import types
import typing

import diagnostic_msgs.msg
import genpy

class DiagnosticStatus(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    OK: byte
    WARN: byte
    ERROR: byte
    STALE: byte

    # Fields
    level: byte
    name: str
    message: str
    hardware_id: str
    values: typing.List[diagnostic_msgs.msg.KeyValue]

    def __init__(
        self,
        level: byte = ...,
        name: str = ...,
        message: str = ...,
        hardware_id: str = ...,
        values: typing.List[diagnostic_msgs.msg.KeyValue] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> DiagnosticStatus: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> DiagnosticStatus: ...
