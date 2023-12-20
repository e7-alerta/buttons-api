import dash.api as dash


def find_one_by_device_id(self, device_id):
    return dash.find_device(device_id)


def find_all_by_devices_type(self, device_type):
    return dash.get_devices(device_type)


def create_or_update_device(self, device):
    return dash.create_or_update(device)


class DevicesRemoteDataSource:

    def __init__(self):
        pass