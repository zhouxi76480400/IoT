import multiprocessing
import asyncio
from config import ConfigReader
import server.TCPServer as TCPServer
import server.UDPServer as UDPServer
import time
import os

# load devices
import dev.DHT11 as DHT11


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
    print("start_fc_light_service pid:" + str(os.getpid()))
    # while True:
    #     print("test")
    #     time.sleep(3)


def start_dht_11_weather_sensor_service():
    print("start_dht_11_weather_sensor_service" + str(os.getpgid()))
    dht11 = DHT11()
    dht11.start_refresh()

processes = 3

# create processes array
process_func_array = [run_server_process, start_fc_light_service, start_dht_11_weather_sensor_service]
# create a processes pool
pool = multiprocessing.Pool(processes=processes)
# start processes
for a_process in process_func_array:
    pool.apply_async(func=a_process)
pool.join()
