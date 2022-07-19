import types
import typing

import control_msgs.msg
import genpy
import trajectory_msgs.msg

class FollowJointTrajectoryGoal(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    trajectory: trajectory_msgs.msg.JointTrajectory
    path_tolerance: typing.List[control_msgs.msg.JointTolerance]
    goal_tolerance: typing.List[control_msgs.msg.JointTolerance]
    goal_time_tolerance: genpy.Duration

    def __init__(
        self,
        trajectory: trajectory_msgs.msg.JointTrajectory = ...,
        path_tolerance: typing.List[control_msgs.msg.JointTolerance] = ...,
        goal_tolerance: typing.List[control_msgs.msg.JointTolerance] = ...,
        goal_time_tolerance: genpy.Duration = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> FollowJointTrajectoryGoal: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> FollowJointTrajectoryGoal: ...
