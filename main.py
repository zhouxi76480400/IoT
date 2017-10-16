from config import ConfigReader
import asyncio
import server.TCPServer
import server.UDPServer


# get config object
config = ConfigReader.get_config()

# init tcp server
tcp_server = server.TCPServer.TCPServer()

# init udp server
udp_server = server.UDPServer.UDPServer()


@asyncio.coroutine
def pi_service():
    while True:
        print("pi_service")
        yield from asyncio.sleep(10)


# start event loop
event_loop = asyncio.get_event_loop()
udp_server.start_server(event_loop)
tasks = [tcp_server.start_server(), pi_service()]
event_loop.run_until_complete(asyncio.wait(tasks))
try:
    event_loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    event_loop.close()
