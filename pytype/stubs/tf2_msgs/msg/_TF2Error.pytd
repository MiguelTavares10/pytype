import types
import typing

import genpy

class TF2Error(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    NO_ERROR: int
    LOOKUP_ERROR: int
    CONNECTIVITY_ERROR: int
    EXTRAPOLATION_ERROR: int
    INVALID_ARGUMENT_ERROR: int
    TIMEOUT_ERROR: int
    TRANSFORM_ERROR: int

    # Fields
    error: int
    error_string: str

    def __init__(
        self,
        error: int = ...,
        error_string: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> TF2Error: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> TF2Error: ...
