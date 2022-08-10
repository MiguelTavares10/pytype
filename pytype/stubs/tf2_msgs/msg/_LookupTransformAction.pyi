import types
import typing

import genpy
import tf2_msgs.msg

class LookupTransformAction(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    action_goal: tf2_msgs.msg.LookupTransformActionGoal
    action_result: tf2_msgs.msg.LookupTransformActionResult
    action_feedback: tf2_msgs.msg.LookupTransformActionFeedback

    def __init__(
        self,
        action_goal: tf2_msgs.msg.LookupTransformActionGoal = ...,
        action_result: tf2_msgs.msg.LookupTransformActionResult = ...,
        action_feedback: tf2_msgs.msg.LookupTransformActionFeedback = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> LookupTransformAction: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> LookupTransformAction: ...
