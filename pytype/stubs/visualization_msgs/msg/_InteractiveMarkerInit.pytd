import types
import typing

import genpy
import visualization_msgs.msg

class InteractiveMarkerInit(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    server_id: str
    seq_num: int
    markers: typing.List[visualization_msgs.msg.InteractiveMarker]

    def __init__(
        self,
        server_id: str = ...,
        seq_num: int = ...,
        markers: typing.List[visualization_msgs.msg.InteractiveMarker] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> InteractiveMarkerInit: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> InteractiveMarkerInit: ...
