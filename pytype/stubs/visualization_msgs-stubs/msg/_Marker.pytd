import types
import typing

import genpy
import geometry_msgs.msg
import std_msgs.msg

class Marker(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    ARROW: int
    CUBE: int
    SPHERE: int
    CYLINDER: int
    LINE_STRIP: int
    LINE_LIST: int
    CUBE_LIST: int
    SPHERE_LIST: int
    POINTS: int
    TEXT_VIEW_FACING: int
    MESH_RESOURCE: int
    TRIANGLE_LIST: int
    ADD: int
    MODIFY: int
    DELETE: int
    DELETEALL: int

    # Fields
    header: std_msgs.msg.Header
    ns: str
    id: int
    type: int
    action: int
    pose: geometry_msgs.msg.Pose
    scale: geometry_msgs.msg.Vector3
    color: std_msgs.msg.ColorRGBA
    lifetime: genpy.Duration
    frame_locked: bool
    points: typing.List[geometry_msgs.msg.Point]
    colors: typing.List[std_msgs.msg.ColorRGBA]
    text: str
    mesh_resource: str
    mesh_use_embedded_materials: bool

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        ns: str = ...,
        id: int = ...,
        type: int = ...,
        action: int = ...,
        pose: geometry_msgs.msg.Pose = ...,
        scale: geometry_msgs.msg.Vector3 = ...,
        color: std_msgs.msg.ColorRGBA = ...,
        lifetime: genpy.Duration = ...,
        frame_locked: bool = ...,
        points: typing.List[geometry_msgs.msg.Point] = ...,
        colors: typing.List[std_msgs.msg.ColorRGBA] = ...,
        text: str = ...,
        mesh_resource: str = ...,
        mesh_use_embedded_materials: bool = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> Marker: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> Marker: ...
