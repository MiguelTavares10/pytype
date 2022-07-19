import types
import typing

import genpy

class ODEJointProperties(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    damping: typing.List[float]
    hiStop: typing.List[float]
    loStop: typing.List[float]
    erp: typing.List[float]
    cfm: typing.List[float]
    stop_erp: typing.List[float]
    stop_cfm: typing.List[float]
    fudge_factor: typing.List[float]
    fmax: typing.List[float]
    vel: typing.List[float]

    def __init__(
        self,
        damping: typing.List[float] = ...,
        hiStop: typing.List[float] = ...,
        loStop: typing.List[float] = ...,
        erp: typing.List[float] = ...,
        cfm: typing.List[float] = ...,
        stop_erp: typing.List[float] = ...,
        stop_cfm: typing.List[float] = ...,
        fudge_factor: typing.List[float] = ...,
        fmax: typing.List[float] = ...,
        vel: typing.List[float] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> ODEJointProperties: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> ODEJointProperties: ...
