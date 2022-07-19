import types
import typing

import genpy
import sensor_msgs.msg

class JoyFeedbackArray(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    array: typing.List[sensor_msgs.msg.JoyFeedback]

    def __init__(
        self,
        array: typing.List[sensor_msgs.msg.JoyFeedback] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> JoyFeedbackArray: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> JoyFeedbackArray: ...
