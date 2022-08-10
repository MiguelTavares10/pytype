import types
import typing

import genpy
import std_msgs.msg
import trajectory_msgs.msg

class MultiDOFJointTrajectory(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    joint_names: typing.List[str]
    points: typing.List[trajectory_msgs.msg.MultiDOFJointTrajectoryPoint]

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        joint_names: typing.List[str] = ...,
        points: typing.List[trajectory_msgs.msg.MultiDOFJointTrajectoryPoint] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> MultiDOFJointTrajectory: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> MultiDOFJointTrajectory: ...
