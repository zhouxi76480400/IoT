import json


# be const
config_file_name = "config.txt"  # filename
config_ver_key = 'ver'  # version
config_devices_key = "devices"  # devices


# a class of config
class Config(object):
    version = 0
    devices = None
    pass


# a device description object
class Device(object):
    id = -1
    name = None
    desc = None
    pass


# allocate a config class
config_class = Config()


# get Config class
def get_config():
    return config_class


# will auto perform this function
def init_config():
    init_config_file_object = open("../" + config_file_name, encoding='utf-8')
    try:
        init_config_all_text = init_config_file_object.read()
    except Exception as e:
        print(e)
        raise e
    finally:
        init_config_file_object.close()
    if init_config_all_text:
        # init Config class
        init_config_all_text = init_config_all_text.strip().split("\n")
        for init_config_item in init_config_all_text:
            init_config_item_key_and_value = init_config_item.strip().split("=")
            init_config_item_key = init_config_item_key_and_value[0]
            init_config_item_value = init_config_item_key_and_value[1]
            # read version
            if init_config_item_key == config_ver_key:
                config_class.version = init_config_item_value
            # init devices
            elif init_config_item_key == config_devices_key:
                config_class.devices = get_devices(init_config_item_value)


def get_devices(file_name):
    # devices
    devices_list = []
    get_devices_file_object = open("../" + file_name, encoding='utf-8')
    try:
        get_devices_all_json = json.load(get_devices_file_object)
    except Exception as e:
        print(e)
        raise e
    finally:
        get_devices_file_object.close()
    if get_devices_all_json:
        for a_json_object in get_devices_all_json:
            device = Device()
            device.name = a_json_object["name"]
            device.desc = a_json_object["desc"]
            device.id = a_json_object["id"]
            print("load device "+device.name)
            devices_list.append(device)
    return devices_list


# auto load
init_config()
