import types
import typing

import genpy
import geometry_msgs.msg

class Transform(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    translation: geometry_msgs.msg.Vector3
    rotation: geometry_msgs.msg.Quaternion

    def __init__(
        self,
        translation: geometry_msgs.msg.Vector3 = ...,
        rotation: geometry_msgs.msg.Quaternion = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> Transform: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> Transform: ...
