import types
import typing

import genpy

class TopicStatistics(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    topic: str
    node_pub: str
    node_sub: str
    window_start: genpy.Time
    window_stop: genpy.Time
    delivered_msgs: int
    dropped_msgs: int
    traffic: int
    period_mean: genpy.Duration
    period_stddev: genpy.Duration
    period_max: genpy.Duration
    stamp_age_mean: genpy.Duration
    stamp_age_stddev: genpy.Duration
    stamp_age_max: genpy.Duration

    def __init__(
        self,
        topic: str = ...,
        node_pub: str = ...,
        node_sub: str = ...,
        window_start: genpy.Time = ...,
        window_stop: genpy.Time = ...,
        delivered_msgs: int = ...,
        dropped_msgs: int = ...,
        traffic: int = ...,
        period_mean: genpy.Duration = ...,
        period_stddev: genpy.Duration = ...,
        period_max: genpy.Duration = ...,
        stamp_age_mean: genpy.Duration = ...,
        stamp_age_stddev: genpy.Duration = ...,
        stamp_age_max: genpy.Duration = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> TopicStatistics: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> TopicStatistics: ...
