import types
import typing

import genpy

class JointTrajectoryPoint(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    positions: typing.List[float]
    velocities: typing.List[float]
    accelerations: typing.List[float]
    effort: typing.List[float]
    time_from_start: genpy.Duration

    def __init__(
        self,
        positions: typing.List[float] = ...,
        velocities: typing.List[float] = ...,
        accelerations: typing.List[float] = ...,
        effort: typing.List[float] = ...,
        time_from_start: genpy.Duration = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> JointTrajectoryPoint: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> JointTrajectoryPoint: ...
