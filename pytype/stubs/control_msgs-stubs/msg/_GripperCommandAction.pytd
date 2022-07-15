import types
import typing

import control_msgs.msg
import genpy

class GripperCommandAction(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    action_goal: control_msgs.msg.GripperCommandActionGoal
    action_result: control_msgs.msg.GripperCommandActionResult
    action_feedback: control_msgs.msg.GripperCommandActionFeedback

    def __init__(
        self,
        action_goal: control_msgs.msg.GripperCommandActionGoal = ...,
        action_result: control_msgs.msg.GripperCommandActionResult = ...,
        action_feedback: control_msgs.msg.GripperCommandActionFeedback = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GripperCommandAction: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GripperCommandAction: ...
