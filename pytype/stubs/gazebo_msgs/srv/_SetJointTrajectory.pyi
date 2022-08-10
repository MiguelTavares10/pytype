import types
import typing

import genpy
import geometry_msgs.msg
import trajectory_msgs.msg

class SetJointTrajectoryRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    model_name: str
    joint_trajectory: trajectory_msgs.msg.JointTrajectory
    model_pose: geometry_msgs.msg.Pose
    set_model_pose: bool
    disable_physics_updates: bool

    def __init__(
        self,
        model_name: str = ...,
        joint_trajectory: trajectory_msgs.msg.JointTrajectory = ...,
        model_pose: geometry_msgs.msg.Pose = ...,
        set_model_pose: bool = ...,
        disable_physics_updates: bool = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> SetJointTrajectoryRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SetJointTrajectoryRequest: ...

class SetJointTrajectoryResponse(genpy.Message):
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
    def deserialize(self, str: bytes) -> SetJointTrajectoryResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SetJointTrajectoryResponse: ...

class SetJointTrajectory(object):
    _type: str
    _md5sum: str
    _request_class = SetJointTrajectoryRequest
    _response_class = SetJointTrajectoryResponse
