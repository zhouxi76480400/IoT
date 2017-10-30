import multiprocessing
import asyncio
from config import ConfigReader
import server.TCPServer as TCPServer
import server.UDPServer as UDPServer
import time
import os


# server for tcp and udp
def run_server_process():
    print("start run_server_process pid:" + str(os.getpid()))
    # get config object
    config = ConfigReader.get_config()
    # init tcp server
    tcp_server = TCPServer.TCPServer()
    # init udp server
    udp_server = UDPServer.UDPServer()
    # start event loop
    event_loop = asyncio.get_event_loop()
    udp_server.start_server(event_loop)
    tasks = [tcp_server.start_server()]
    event_loop.run_until_complete(asyncio.wait(tasks))
    try:
        event_loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        event_loop.close()


# device FCLight light sensor
def start_fc_light_service():
    import dev.FCLight as FCLight
    print("start_fc_light_service pid:" + str(os.getpid()))
    fc_light = FCLight.FCLight()
    fc_light.start_service()


def start_dht_11_weather_sensor_service():
    import dev.DHT11 as DHT11
    print("start_dht_11_weather_sensor_service pid:" + str(os.getpid()))
    dht11 = DHT11.DHT11()
    dht11.start_refresh()


def start_nfc_module_use_python2():
    print("start_nfc_module_use_python2: process pid:" + str(os.getpid()))
    dev_path = ConfigReader.get_dev_full_path()
    script_path = os.path.join(os.path.join(dev_path, 'beam_py_2'), 'start.sh')
    print(script_path)
    os.system(script_path)




# create processes array
process_func_array = [run_server_process, start_nfc_module_use_python2, start_fc_light_service, start_dht_11_weather_sensor_service]
# create a processes pool
pool = multiprocessing.Pool(processes=len(process_func_array))
# start processes
for a_process in process_func_array:
    pool.apply_async(func=a_process)
pool.close()
pool.join()
