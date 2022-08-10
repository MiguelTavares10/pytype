import types
import typing

import genpy
import geometry_msgs.msg
import tf2_msgs.msg

class LookupTransformResult(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    transform: geometry_msgs.msg.TransformStamped
    error: tf2_msgs.msg.TF2Error

    def __init__(
        self,
        transform: geometry_msgs.msg.TransformStamped = ...,
        error: tf2_msgs.msg.TF2Error = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> LookupTransformResult: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> LookupTransformResult: ...
