

class DeviceRepository(object):

    def __init__(self, device_data_source):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def get_devices(self):
        return self.devices

    def find_by_device_type(self, device_type):
        devices = []
        for device in self.devices:
            if device.device_type == device_type:
                devices.append(device)
        return devices

    def find_by_id(self, device_id):
        for device in self.devices:
            if device.id == device_id:
                return device
        return None
