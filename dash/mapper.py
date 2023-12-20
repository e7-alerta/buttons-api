from dash.types import Device, DeviceStatus, DeviceType



def device_load(item):
    print(item)
    return Device(
        id=item["id"],
        status=DeviceStatus(item["status"]),
        alerted=item["alerted"],
        sos=item["sos"],
        device_type=DeviceType(item["device_type"]),
        device_id=item["device_id"],
        name=item["device_name"],
        tuya_device=item["tuya_device"],
        tuya_id=item["tuya_id"],
        place_id=item["place"]
    )
