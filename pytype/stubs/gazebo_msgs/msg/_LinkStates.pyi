import types
import typing

import genpy
import geometry_msgs.msg

class LinkStates(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    name: typing.List[str]
    pose: typing.List[geometry_msgs.msg.Pose]
    twist: typing.List[geometry_msgs.msg.Twist]

    def __init__(
        self,
        name: typing.List[str] = ...,
        pose: typing.List[geometry_msgs.msg.Pose] = ...,
        twist: typing.List[geometry_msgs.msg.Twist] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> LinkStates: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> LinkStates: ...
