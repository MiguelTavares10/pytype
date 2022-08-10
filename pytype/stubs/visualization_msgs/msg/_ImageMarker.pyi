import types
import typing

import genpy
import geometry_msgs.msg
import std_msgs.msg

class ImageMarker(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    CIRCLE: int
    LINE_STRIP: int
    LINE_LIST: int
    POLYGON: int
    POINTS: int
    ADD: int
    REMOVE: int

    # Fields
    header: std_msgs.msg.Header
    ns: str
    id: int
    type: int
    action: int
    position: geometry_msgs.msg.Point
    scale: float
    outline_color: std_msgs.msg.ColorRGBA
    filled: int
    fill_color: std_msgs.msg.ColorRGBA
    lifetime: genpy.Duration
    points: typing.List[geometry_msgs.msg.Point]
    outline_colors: typing.List[std_msgs.msg.ColorRGBA]

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        ns: str = ...,
        id: int = ...,
        type: int = ...,
        action: int = ...,
        position: geometry_msgs.msg.Point = ...,
        scale: float = ...,
        outline_color: std_msgs.msg.ColorRGBA = ...,
        filled: int = ...,
        fill_color: std_msgs.msg.ColorRGBA = ...,
        lifetime: genpy.Duration = ...,
        points: typing.List[geometry_msgs.msg.Point] = ...,
        outline_colors: typing.List[std_msgs.msg.ColorRGBA] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> ImageMarker: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> ImageMarker: ...
