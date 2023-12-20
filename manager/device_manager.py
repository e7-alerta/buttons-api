import uuid

import slugify as slugify

from dash.types import Device, DeviceType, DeviceStatus
from data.repositories import device_repository


def draft_device_of(device_type: DeviceType,
                    id=None,
                    device_id=None,
                    tuya_device: bool = False,
                    tuya_id: str = None,
                    status: DeviceStatus = DeviceStatus.DRAFT,
                    alerted=False,
                    sos=False
                    ) -> Device:
    """
    Draft a device by its device id.
    :param device_id
    :param status
    :param alerted
    :param device_type
    :return: the device
    """
    if id is None:
        id = str(uuid.uuid4())

    name = slugify.slugify(device_type.value + " " + str(uuid.uuid4())[0:4])

    device = Device(
        id=id,
        name=name,
        device_id=device_id,
        status=status,
        alerted=alerted,
        sos=sos,
        device_type=device_type
    )
    return device


def find_by_tuya_id(tuya_id: str) -> None | Device:
    device = device_repository.find_one_by_tuya_id(tuya_id)
    return device


def find_or_create_device_by_id(phonebtn_id):
    """
    Find or create a device by its device id.
    :param phonebtn_id: the device id
    :return: the device
    """
    device = device_repository.find_one_by_device_id(phonebtn_id)
    if device is None:
        device = device_repository.create(draft_device_of(
            device_id=phonebtn_id,
            device_type=DeviceType.PHONE_BUTTON
        ))
    return device


def alert_device(device: Device, sos = False):
    """
    Alert a device.
    :param sos:
    :param device:
    :return:
    """
    device.alerted = True
    device.sos = sos
    device_repository.update(device)
    return None
