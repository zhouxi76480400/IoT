import json
import os


# be const
config_file_name = "config.txt"  # filename
config_ver_key = 'ver'  # version
config_devices_key = "devices"  # devices
config_password_file_name = "pwd"  # password_file_name

project_path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])


# a class of config
class Config(object):
    version = 0
    devices = None
    host_name = None
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
    init_config_file_object = open(project_path + "/" + config_file_name, encoding='utf-8')
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
        import socket
        config_class.host_name = socket.gethostname()


def get_devices(file_name):
    # devices
    devices_list = []
    get_devices_file_object = open(project_path + "/" + file_name, encoding='utf-8')
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


def check_password_file_exist():
    check_password_file_exist_full_path = os.path.join(project_path, config_password_file_name)
    if os.path.exists(check_password_file_exist_full_path):
        return True
    return False


# setpassword
def create_password_file(password):
    print(password)
    create_password_file_full_path = os.path.join(project_path, config_password_file_name)
    if check_password_file_exist():
        os.remove(create_password_file_full_path)
    # write file
    create_password_file_output = open(create_password_file_full_path, 'w')
    create_password_file_output.write(password)
    create_password_file_output.close()


# check pwd
def check_password(wait_check_password):
    if check_password_file_exist():
        print(wait_check_password)
        check_password_file_full_path = os.path.join(project_path, config_password_file_name)
        check_password_input = open(check_password_file_full_path, encoding='utf-8')
        try:
            check_password_true_pwd = check_password_input.read()
        except Exception as e:
            print(e)
            raise e
        finally:
            check_password_input.close()
        if check_password_true_pwd:
            if wait_check_password == check_password_true_pwd:
                return True
    return False


# auto load
init_config()
