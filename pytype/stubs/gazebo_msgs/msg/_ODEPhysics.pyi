import types
import typing

import genpy

class ODEPhysics(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    auto_disable_bodies: bool
    sor_pgs_precon_iters: int
    sor_pgs_iters: int
    sor_pgs_w: float
    sor_pgs_rms_error_tol: float
    contact_surface_layer: float
    contact_max_correcting_vel: float
    cfm: float
    erp: float
    max_contacts: int

    def __init__(
        self,
        auto_disable_bodies: bool = ...,
        sor_pgs_precon_iters: int = ...,
        sor_pgs_iters: int = ...,
        sor_pgs_w: float = ...,
        sor_pgs_rms_error_tol: float = ...,
        contact_surface_layer: float = ...,
        contact_max_correcting_vel: float = ...,
        cfm: float = ...,
        erp: float = ...,
        max_contacts: int = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> ODEPhysics: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> ODEPhysics: ...
