import config.ConfigReader
import json

api_json = json.load(open(config.ConfigReader.project_path + "/api.json"))
# all api dictionary
api_json_dictionary = {}
# get api_json_dictionary
for api_json_object in api_json:
    api_json_object_key = api_json_object['key']
    api_json_object_value = api_json_object['value']
    api_json_dictionary[api_json_object_key] = api_json_object_value


# handle all request and return
def handleRequest(request_params):
    # split request
    request_name_and_value = request_params.split(':')
    # request name
    request_name = request_name_and_value[0]
    # request property
    request_property = request_name_and_value[1]
    # to call this method
    method_name = api_json_dictionary[request_name]
    if not method_name:
        # not support params
        return ''
    # perform
    resp_str = eval(method_name)(request_property)
    return appendResponse(resp_str)


# add end format
def appendResponse(resp):
    all_resp = resp + '\0'
    return all_resp


# GetAllDevicesList method
def GetAllDevicesList(params):
    str_all = open(config.ConfigReader.project_path + "/devices.json", encoding='utf-8').read()
    return str_all


# CheckPasswordExist
def IsServerHavePassword(params):
    return str(config.ConfigReader.check_password_file_exist()).lower()


# Set PWD
def SetServersPassword(params):
    int_set_servers_password = len(params)
    if int_set_servers_password < 6 or int_set_servers_password > 20:
        return str(False).lower()
    # start write pwd
    config.ConfigReader.create_password_file(params)
    return str(True).lower()


# check pwd
def PasswordAuthentication(params):
    return str(config.ConfigReader.check_password(params)).lower()


#
def GetNFCCard(params):
    get_nfc_card_split = str(params).split(',')
    get_nfc_card_pwd = get_nfc_card_split[0]
    get_nfc_card_time = get_nfc_card_split[1]
    get_nfc_card_pwd_check = config.ConfigReader.check_password(get_nfc_card_pwd)
    if get_nfc_card_pwd_check:
        key_object = config.ConfigReader.generator_a_nfc_password(get_nfc_card_pwd, get_nfc_card_time)
        dic = {"time": key_object.create_time, "key": key_object.key}
        return str(dic)
    return str(False)


def GetAllNFCAuthOKData(params):
    get_all_nfc_auth_ok_data_all_records = config.ConfigReader.get_all_record_data()
    return get_all_nfc_auth_ok_data_all_records
