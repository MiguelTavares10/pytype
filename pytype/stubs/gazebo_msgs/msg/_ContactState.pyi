import types
import typing

import genpy
import geometry_msgs.msg

class ContactState(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    info: str
    collision1_name: str
    collision2_name: str
    wrenches: typing.List[geometry_msgs.msg.Wrench]
    total_wrench: geometry_msgs.msg.Wrench
    contact_positions: typing.List[geometry_msgs.msg.Vector3]
    contact_normals: typing.List[geometry_msgs.msg.Vector3]
    depths: typing.List[float]

    def __init__(
        self,
        info: str = ...,
        collision1_name: str = ...,
        collision2_name: str = ...,
        wrenches: typing.List[geometry_msgs.msg.Wrench] = ...,
        total_wrench: geometry_msgs.msg.Wrench = ...,
        contact_positions: typing.List[geometry_msgs.msg.Vector3] = ...,
        contact_normals: typing.List[geometry_msgs.msg.Vector3] = ...,
        depths: typing.List[float] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> ContactState: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> ContactState: ...
