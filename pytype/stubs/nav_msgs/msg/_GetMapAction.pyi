import types
import typing

import genpy
import nav_msgs.msg

class GetMapAction(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    action_goal: nav_msgs.msg.GetMapActionGoal
    action_result: nav_msgs.msg.GetMapActionResult
    action_feedback: nav_msgs.msg.GetMapActionFeedback

    def __init__(
        self,
        action_goal: nav_msgs.msg.GetMapActionGoal = ...,
        action_result: nav_msgs.msg.GetMapActionResult = ...,
        action_feedback: nav_msgs.msg.GetMapActionFeedback = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GetMapAction: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GetMapAction: ...
