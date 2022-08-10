import types
import typing

import genpy
import geometry_msgs.msg
import std_msgs.msg

class InteractiveMarkerFeedback(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    KEEP_ALIVE: int
    POSE_UPDATE: int
    MENU_SELECT: int
    BUTTON_CLICK: int
    MOUSE_DOWN: int
    MOUSE_UP: int

    # Fields
    header: std_msgs.msg.Header
    client_id: str
    marker_name: str
    control_name: str
    event_type: int
    pose: geometry_msgs.msg.Pose
    menu_entry_id: int
    mouse_point: geometry_msgs.msg.Point
    mouse_point_valid: bool

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        client_id: str = ...,
        marker_name: str = ...,
        control_name: str = ...,
        event_type: int = ...,
        pose: geometry_msgs.msg.Pose = ...,
        menu_entry_id: int = ...,
        mouse_point: geometry_msgs.msg.Point = ...,
        mouse_point_valid: bool = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> InteractiveMarkerFeedback: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> InteractiveMarkerFeedback: ...
