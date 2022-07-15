import types
import typing

import actionlib_msgs.msg
import control_msgs.msg
import genpy
import std_msgs.msg

class GripperCommandActionFeedback(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    status: actionlib_msgs.msg.GoalStatus
    feedback: control_msgs.msg.GripperCommandFeedback

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        status: actionlib_msgs.msg.GoalStatus = ...,
        feedback: control_msgs.msg.GripperCommandFeedback = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GripperCommandActionFeedback: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GripperCommandActionFeedback: ...
