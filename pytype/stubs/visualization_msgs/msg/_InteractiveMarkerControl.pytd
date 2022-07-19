import types
import typing

import genpy
import geometry_msgs.msg
import visualization_msgs.msg

class InteractiveMarkerControl(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    INHERIT: int
    FIXED: int
    VIEW_FACING: int
    NONE: int
    MENU: int
    BUTTON: int
    MOVE_AXIS: int
    MOVE_PLANE: int
    ROTATE_AXIS: int
    MOVE_ROTATE: int
    MOVE_3D: int
    ROTATE_3D: int
    MOVE_ROTATE_3D: int

    # Fields
    name: str
    orientation: geometry_msgs.msg.Quaternion
    orientation_mode: int
    interaction_mode: int
    always_visible: bool
    markers: typing.List[visualization_msgs.msg.Marker]
    independent_marker_orientation: bool
    description: str

    def __init__(
        self,
        name: str = ...,
        orientation: geometry_msgs.msg.Quaternion = ...,
        orientation_mode: int = ...,
        interaction_mode: int = ...,
        always_visible: bool = ...,
        markers: typing.List[visualization_msgs.msg.Marker] = ...,
        independent_marker_orientation: bool = ...,
        description: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> InteractiveMarkerControl: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> InteractiveMarkerControl: ...
