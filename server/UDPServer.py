import asyncio
import server.UDPRequestHandler

BUFF_SIZE = 1024

UDP_PORT = 20001

UDP_SEND_PORT = UDP_PORT + 1


class UDPServer(object):
    _instance = None
    transport = None

    # singleton
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(UDPServer, cls).__new__(cls)
        return cls._instance

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, address):
        # message = data.decode()
        # print('Received %r from %s' % (message, address))
        # print('Send %r to %s' % (message, address))
        resp = server.UDPRequestHandler.handleRequest(self=self, data=data, address=address)
        send_to_address = (address[0], UDP_SEND_PORT)
        print("send to address :"+address[0])
        print("send to port :"+str(UDP_SEND_PORT))
        self.transport.sendto(bytes(resp, encoding='utf-8'), send_to_address)

    @staticmethod
    def error_received(self, error):
        print("test"+str(self)+str(error))

    @staticmethod
    def connection_lost(self):
        print(str(self)+"connection_lost")

    def start_server(self, loop):
        print("Start UDP Server")
        listen = loop.create_datagram_endpoint(UDPServer, local_addr=('0.0.0.0', UDP_PORT), allow_broadcast=True)
        self.transport, protocol = loop.run_until_complete(listen)
        # self.transport.close()

    pass

