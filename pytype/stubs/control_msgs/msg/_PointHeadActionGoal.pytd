import types
import typing

import actionlib_msgs.msg
import control_msgs.msg
import genpy
import std_msgs.msg

class PointHeadActionGoal(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    goal_id: actionlib_msgs.msg.GoalID
    goal: control_msgs.msg.PointHeadGoal

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        goal_id: actionlib_msgs.msg.GoalID = ...,
        goal: control_msgs.msg.PointHeadGoal = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> PointHeadActionGoal: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> PointHeadActionGoal: ...
