import dash.api.devices_api as dash
from dash.types import Device


def find_one_by_tuya_id(tuya_id) -> None | Device:
    return dash.find_one_by_tuya_id(tuya_id)


def find_one_by_device_id(device_id) -> None | Device:
    return dash.find_one_by_device_id(device_id)


def create(device: Device) -> Device:
    return dash.create(device)


def update(device: Device) -> Device:
    return dash.update(device)
