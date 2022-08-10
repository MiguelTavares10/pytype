import types
import typing

import genpy
import std_msgs.msg

class BatteryState(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    POWER_SUPPLY_STATUS_UNKNOWN: int
    POWER_SUPPLY_STATUS_CHARGING: int
    POWER_SUPPLY_STATUS_DISCHARGING: int
    POWER_SUPPLY_STATUS_NOT_CHARGING: int
    POWER_SUPPLY_STATUS_FULL: int
    POWER_SUPPLY_HEALTH_UNKNOWN: int
    POWER_SUPPLY_HEALTH_GOOD: int
    POWER_SUPPLY_HEALTH_OVERHEAT: int
    POWER_SUPPLY_HEALTH_DEAD: int
    POWER_SUPPLY_HEALTH_OVERVOLTAGE: int
    POWER_SUPPLY_HEALTH_UNSPEC_FAILURE: int
    POWER_SUPPLY_HEALTH_COLD: int
    POWER_SUPPLY_HEALTH_WATCHDOG_TIMER_EXPIRE: int
    POWER_SUPPLY_HEALTH_SAFETY_TIMER_EXPIRE: int
    POWER_SUPPLY_TECHNOLOGY_UNKNOWN: int
    POWER_SUPPLY_TECHNOLOGY_NIMH: int
    POWER_SUPPLY_TECHNOLOGY_LION: int
    POWER_SUPPLY_TECHNOLOGY_LIPO: int
    POWER_SUPPLY_TECHNOLOGY_LIFE: int
    POWER_SUPPLY_TECHNOLOGY_NICD: int
    POWER_SUPPLY_TECHNOLOGY_LIMN: int

    # Fields
    header: std_msgs.msg.Header
    voltage: float
    temperature: float
    current: float
    charge: float
    capacity: float
    design_capacity: float
    percentage: float
    power_supply_status: int
    power_supply_health: int
    power_supply_technology: int
    present: bool
    cell_voltage: typing.List[float]
    cell_temperature: typing.List[float]
    location: str
    serial_number: str

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        voltage: float = ...,
        temperature: float = ...,
        current: float = ...,
        charge: float = ...,
        capacity: float = ...,
        design_capacity: float = ...,
        percentage: float = ...,
        power_supply_status: int = ...,
        power_supply_health: int = ...,
        power_supply_technology: int = ...,
        present: bool = ...,
        cell_voltage: typing.List[float] = ...,
        cell_temperature: typing.List[float] = ...,
        location: str = ...,
        serial_number: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> BatteryState: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> BatteryState: ...
