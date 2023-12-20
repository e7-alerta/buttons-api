from enum import Enum

import requests

from dash.mapper import device_load
from dash.types import DeviceStatus, DeviceType, Device


def find_one_by_tuya_id(tuya_id: str) -> None | Device:
    url = "https://dash.vecinos.com.ar/items/iot_devices"

    querystring = {
        "filter[status][_eq]": "enabled",
        "limit": "1",
    }

    if not tuya_id:
        raise ValueError("tuya_id is required")

    querystring["filter[tuya_id][_eq]"] = tuya_id

    response = requests.request("GET", url, params=querystring)
    data = response.json()["data"]

    if not data:
        return None

    device = device_load(data[0])
    return device


def find_one_by_device_id(device_id: str) -> None | Device:
    url = "https://dash.vecinos.com.ar/items/iot_devices"

    querystring = {
        "limit": "1",
    }

    if not device_id:
        raise ValueError("device_id is required")

    querystring["filter[device_id][_eq]"] = device_id

    response = requests.request("GET", url, params=querystring)
    data = response.json()["data"]

    if not data:
        return None

    print(data[0])
    device = device_load(data[0])
    return device


def get_devices(device_type: DeviceType = None):
    # status = "activated"

    url = "https://dash.vecinos.com.ar/items/iot_devices"

    querystring = {
        "filter[status][_eq]": "enabled",
        "limit": "20"
    }

    if device_type:
        querystring["filter[device_type][_eq]"] = device_type.value

    response = requests.request("GET", url, params=querystring)
    data = response.json()["data"]

    devices = []
    for item in data:
        device = device_load(item)
        devices.append(
            device
        )
    return devices


def create(device: Device) -> Device:
    print("create device ", device)
    url = "https://dash.vecinos.com.ar/items/iot_devices"

    payload = {
        "id": device.id,
        "device_name": device.name,
        "tuya_id": device.tuya_id,
        "tuya_device": device.tuya_device,
        "device_id": device.device_id,
        "device_type": device.device_type.value,
        "alerted": device.alerted,
        "sos": device.sos,
        "status": device.status.value
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, json=payload)
    data = response.json()["data"]
    device = device_load(data)
    return device


def update(device: Device) -> Device:
    url = f"https://dash.vecinos.com.ar/items/iot_devices/{device.id}"

    payload = {
        "alerted": device.alerted,
        "sos": device.sos,
        "status": device.status.value
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, json=payload)
    data = response.json()["data"]
    device = device_load(data)
    return device


def mark_device_alerted(device_id: str):
    # url = f"https://dash.vecinos.com.ar/items/iot_devices/{device_id}"
    url = f"http://0.0.0.0:5070/items/iot_devices/{device_id}"
    payload = {
        "alerted": True,
        "status": DeviceStatus.ACTIVATED.value
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("PATCH", url, headers=headers, json=payload)
    return response


if __name__ == '__main__':
    devices = get_devices()
    print(devices)
    mark_device_alerted(devices[0].id)
