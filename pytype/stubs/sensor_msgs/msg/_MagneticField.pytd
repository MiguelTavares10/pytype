import types
import typing

import genpy
import geometry_msgs.msg
import std_msgs.msg

class MagneticField(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    magnetic_field: geometry_msgs.msg.Vector3
    magnetic_field_covariance: typing.List[float]

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        magnetic_field: geometry_msgs.msg.Vector3 = ...,
        magnetic_field_covariance: typing.List[float] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> MagneticField: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> MagneticField: ...
