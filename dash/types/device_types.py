import uuid
from enum import Enum
from typing import Optional

from pydantic import BaseModel, UUID4


class DeviceType(Enum):
    MINI_ALARM = "mini_alarm"
    DOOR_CONTACT = "door_contact"
    PHONE_BUTTON = "phone_button"
    ALARM_BUTTON = "alarm_button"
    MOTION_SENSOR = "motion_sensor"
    LIGHT_SENSOR = "light_sensor"
    CAMERA = "camera"
    WINDOW = "window"
    GARAGE_DOOR = "garage_door"
    DOOR_LOCK = "door_lock"
    DOOR_BELL = "door_bell"


class DeviceStatus(Enum):
    DRAFT = "draft"
    ENABLED = "enabled"
    ACTIVATED = "activated"
    DISABLED = "disabled"
    PUBLISHED = "published"
    pass


class Device(BaseModel):
    id: str
    status: DeviceStatus
    alerted: bool = False
    sos: bool = False
    device_type: DeviceType
    name: Optional[str] = None
    tuya_device: bool = False
    device_id: Optional[str] = None
    params: Optional[dict] = None
    tuya_id: Optional[str] = None
    place_id: Optional[str] = None


