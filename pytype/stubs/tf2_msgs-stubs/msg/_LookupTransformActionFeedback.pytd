import types
import typing

import actionlib_msgs.msg
import genpy
import std_msgs.msg
import tf2_msgs.msg

class LookupTransformActionFeedback(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    status: actionlib_msgs.msg.GoalStatus
    feedback: tf2_msgs.msg.LookupTransformFeedback

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        status: actionlib_msgs.msg.GoalStatus = ...,
        feedback: tf2_msgs.msg.LookupTransformFeedback = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> LookupTransformActionFeedback: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> LookupTransformActionFeedback: ...
