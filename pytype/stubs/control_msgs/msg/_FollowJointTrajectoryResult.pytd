import types
import typing

import genpy

class FollowJointTrajectoryResult(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    SUCCESSFUL: int
    INVALID_GOAL: int
    INVALID_JOINTS: int
    OLD_HEADER_TIMESTAMP: int
    PATH_TOLERANCE_VIOLATED: int
    GOAL_TOLERANCE_VIOLATED: int

    # Fields
    error_code: int
    error_string: str

    def __init__(
        self,
        error_code: int = ...,
        error_string: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> FollowJointTrajectoryResult: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> FollowJointTrajectoryResult: ...
