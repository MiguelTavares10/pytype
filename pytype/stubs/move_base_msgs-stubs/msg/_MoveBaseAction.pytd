import types
import typing

import genpy
import move_base_msgs.msg

class MoveBaseAction(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    action_goal: move_base_msgs.msg.MoveBaseActionGoal
    action_result: move_base_msgs.msg.MoveBaseActionResult
    action_feedback: move_base_msgs.msg.MoveBaseActionFeedback

    def __init__(
        self,
        action_goal: move_base_msgs.msg.MoveBaseActionGoal = ...,
        action_result: move_base_msgs.msg.MoveBaseActionResult = ...,
        action_feedback: move_base_msgs.msg.MoveBaseActionFeedback = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> MoveBaseAction: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> MoveBaseAction: ...
