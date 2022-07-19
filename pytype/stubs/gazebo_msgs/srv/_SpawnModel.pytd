import types
import typing

import genpy
import geometry_msgs.msg

class SpawnModelRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    model_name: str
    model_xml: str
    robot_namespace: str
    initial_pose: geometry_msgs.msg.Pose
    reference_frame: str

    def __init__(
        self,
        model_name: str = ...,
        model_xml: str = ...,
        robot_namespace: str = ...,
        initial_pose: geometry_msgs.msg.Pose = ...,
        reference_frame: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> SpawnModelRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SpawnModelRequest: ...

class SpawnModelResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    success: bool
    status_message: str

    def __init__(
        self,
        success: bool = ...,
        status_message: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> SpawnModelResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SpawnModelResponse: ...

class SpawnModel(object):
    _type: str
    _md5sum: str
    _request_class = SpawnModelRequest
    _response_class = SpawnModelResponse
