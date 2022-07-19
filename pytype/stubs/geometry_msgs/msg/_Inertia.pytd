import types
import typing

import genpy
import geometry_msgs.msg

class Inertia(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    m: float
    com: geometry_msgs.msg.Vector3
    ixx: float
    ixy: float
    ixz: float
    iyy: float
    iyz: float
    izz: float

    def __init__(
        self,
        m: float = ...,
        com: geometry_msgs.msg.Vector3 = ...,
        ixx: float = ...,
        ixy: float = ...,
        ixz: float = ...,
        iyy: float = ...,
        iyz: float = ...,
        izz: float = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> Inertia: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> Inertia: ...
