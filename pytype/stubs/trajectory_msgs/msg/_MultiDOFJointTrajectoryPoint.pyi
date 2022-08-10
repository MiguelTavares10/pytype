import types
import typing

import genpy
import geometry_msgs.msg

class MultiDOFJointTrajectoryPoint(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    transforms: typing.List[geometry_msgs.msg.Transform]
    velocities: typing.List[geometry_msgs.msg.Twist]
    accelerations: typing.List[geometry_msgs.msg.Twist]
    time_from_start: genpy.Duration

    def __init__(
        self,
        transforms: typing.List[geometry_msgs.msg.Transform] = ...,
        velocities: typing.List[geometry_msgs.msg.Twist] = ...,
        accelerations: typing.List[geometry_msgs.msg.Twist] = ...,
        time_from_start: genpy.Duration = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> MultiDOFJointTrajectoryPoint: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> MultiDOFJointTrajectoryPoint: ...
