import types
import typing

import genpy

class MenuEntry(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    FEEDBACK: int
    ROSRUN: int
    ROSLAUNCH: int

    # Fields
    id: int
    parent_id: int
    title: str
    command: str
    command_type: int

    def __init__(
        self,
        id: int = ...,
        parent_id: int = ...,
        title: str = ...,
        command: str = ...,
        command_type: int = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> MenuEntry: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> MenuEntry: ...
