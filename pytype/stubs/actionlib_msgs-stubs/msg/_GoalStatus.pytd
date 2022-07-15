import types
import typing

import actionlib_msgs.msg
import genpy

class GoalStatus(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    PENDING: int
    ACTIVE: int
    PREEMPTED: int
    SUCCEEDED: int
    ABORTED: int
    REJECTED: int
    PREEMPTING: int
    RECALLING: int
    RECALLED: int
    LOST: int

    # Fields
    goal_id: actionlib_msgs.msg.GoalID
    status: int
    text: str

    def __init__(
        self,
        goal_id: actionlib_msgs.msg.GoalID = ...,
        status: int = ...,
        text: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GoalStatus: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GoalStatus: ...
