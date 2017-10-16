# #!/usr/bin/env python
# # -*- coding:UTF-8 -*-
#
# from socket import *
# from time import ctime
#
# HOST = '127.0.0.1'
# PORT = 20001
# BUFSIZE = 1024
#
# ADDR = (HOST, PORT)
#
# udpSerSock = socket(AF_INET, SOCK_DGRAM)
# udpSerSock.bind(('', PORT))
# print
# 'wating for message...'
# while True:
#     data, addr = udpSerSock.recvfrom(BUFSIZE)
#     print('...received ->%s  %s' % (addr, data))
#
# udpSerSock.close()

import asyncio

class EchoServerProtocol:
    transport = None
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        print('Received %r from %s' % (message, addr))
        print('Send %r to %s' % (message, addr))
        self.transport.sendto(data, addr)

    def error_received(self,error):
        print("test"+str(error))

loop = asyncio.get_event_loop()
print("Starting UDP server")
# One protocol instance will be created to serve all client requests
listen = loop.create_datagram_endpoint(EchoServerProtocol, local_addr=('0.0.0.0', 20001), allow_broadcast=True)
transport, protocol = loop.run_until_complete(listen)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

transport.close()
loop.close()

# import asyncio
#
# class EchoClientProtocol:
#     def __init__(self, message, loop):
#         self.message = message
#         self.loop = loop
#         self.transport = None
#
#     def connection_made(self, transport):
#         self.transport = transport
#         print('Send:', self.message)
#         self.transport.sendto(self.message.encode())
#
#     def datagram_received(self, data, addr):
#         print("Received:", data.decode())
#
#         print("Close the socket")
#         self.transport.close()
#
#     def error_received(self, exc):
#         print('Error received:', exc)
#
#     def connection_lost(self, exc):
#         print("Socket closed, stop the event loop")
#         loop = asyncio.get_event_loop()
#         loop.stop()
#
# loop = asyncio.get_event_loop()
# message = "Hello World!"
# connect = loop.create_datagram_endpoint(
#     lambda: EchoClientProtocol(message, loop),
#     remote_addr=('127.0.0.1', 20001))
# transport, protocol = loop.run_until_complete(connect)
# loop.run_forever()
# transport.close()
# loop.close()