import json
import config.ConfigReader
# to find action
action_key = 'action'

# key word multi cast
multi_cast_receive = 'findiot'


def handleRequest(self, data, address):
    message = str(data.decode())
    print("udp : " + message)
    json_text = json.loads(message)
    request_action = json_text[action_key]
    response_text = ''
    if request_action == multi_cast_receive:
        request_package_name = json_text['package_name']
        request_version = json_text['version']
        response_text = handle_multi_cast(request_package_name,request_version)

    print("resp : " + response_text)
    return response_text


def handle_multi_cast(package_name, version):
    resp = False
    if package_name == 'me.zhouxi.iot':
        resp = True
    else:
        resp = False
    return str({"action": multi_cast_receive, "resp": resp, "ver": config.ConfigReader.get_config().version, "name": "xxxxx"})
