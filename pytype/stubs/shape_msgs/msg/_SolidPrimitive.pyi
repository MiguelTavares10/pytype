import types
import typing

import genpy

class SolidPrimitive(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    BOX: int
    SPHERE: int
    CYLINDER: int
    CONE: int
    BOX_X: int
    BOX_Y: int
    BOX_Z: int
    SPHERE_RADIUS: int
    CYLINDER_HEIGHT: int
    CYLINDER_RADIUS: int
    CONE_HEIGHT: int
    CONE_RADIUS: int

    # Fields
    type: int
    dimensions: typing.List[float]

    def __init__(
        self,
        type: int = ...,
        dimensions: typing.List[float] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> SolidPrimitive: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SolidPrimitive: ...
