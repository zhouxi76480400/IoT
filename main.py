from config import ConfigReader
import asyncio
import server.TCPServer as TCPServer
import server.UDPServer
import dev.FCLight as FCLight

# get config object
config = ConfigReader.get_config()

# init tcp server
tcp_server = TCPServer.TCPServer()

# init udp server
udp_server = server.UDPServer.UDPServer()

# dev

# light
light = FCLight.FCLight()

# start event loop
event_loop = asyncio.get_event_loop()
udp_server.start_server(event_loop)
tasks = [tcp_server.start_server(), light.start_service()]
event_loop.run_until_complete(asyncio.wait(tasks))
try:
    event_loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    event_loop.close()
    light.stop_service()
