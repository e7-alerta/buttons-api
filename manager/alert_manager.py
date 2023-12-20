from manager import device_manager


def handle_phone_button_alert(phonebtn_id):
    """
    Chequea si el id del boton de panico existe en la base de datos
    si no existe, lo crea  y lo alerta
    si existe, chequea si esta alertado
    si esta alertado, no hace nada
    si no esta alertado, lo alerta
    :param phonebtn_id:
    :return:
    """
    print(f"[phone_button_manager] phonebtn_id: {phonebtn_id}")

    device = device_manager.find_or_create_device_by_id(phonebtn_id)

    if device.alerted:
        print(f"[phone_button_manager] device {phonebtn_id} is already alerted")
        return

    device_manager.alert_device(device, sos=True)
    pass
