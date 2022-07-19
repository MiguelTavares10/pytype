import types
import typing

import genpy
import geometry_msgs.msg
import std_msgs.msg

class MultiDOFJointState(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    joint_names: typing.List[str]
    transforms: typing.List[geometry_msgs.msg.Transform]
    twist: typing.List[geometry_msgs.msg.Twist]
    wrench: typing.List[geometry_msgs.msg.Wrench]

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        joint_names: typing.List[str] = ...,
        transforms: typing.List[geometry_msgs.msg.Transform] = ...,
        twist: typing.List[geometry_msgs.msg.Twist] = ...,
        wrench: typing.List[geometry_msgs.msg.Wrench] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> MultiDOFJointState: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> MultiDOFJointState: ...
