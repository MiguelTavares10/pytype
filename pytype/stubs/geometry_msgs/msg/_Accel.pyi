import types
import typing

import genpy
import geometry_msgs.msg

class Accel(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    linear: geometry_msgs.msg.Vector3
    angular: geometry_msgs.msg.Vector3

    def __init__(
        self,
        linear: geometry_msgs.msg.Vector3 = ...,
        angular: geometry_msgs.msg.Vector3 = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> Accel: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> Accel: ...
