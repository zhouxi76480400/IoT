import config.ConfigReader
import json

api_json = json.load(open(config.ConfigReader.project_path+"/api.json"))
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
    str_all = open("../devices.json", encoding='utf-8').read()
    return str_all
