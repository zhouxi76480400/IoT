import asyncio
import server.RequestHandler

BUFF_SIZE = 1024


class TCPServer(object):
    _instance = None

    def __init__(self):
        print("Start TCP Server")

    # singleton
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TCPServer, cls).__new__(cls)
        return cls._instance

    @asyncio.coroutine
    def start_server(self):
        yield from asyncio.start_server(self.client_connected_handler, '', 20000)

    @asyncio.coroutine
    def client_connected_handler(self, client_reader, client_writer):
        print("Client Connect")
        all_data = ''
        while True:
            data = yield from client_reader.read(BUFF_SIZE)
            data_str = str(data, encoding='utf-8')
            all_data = all_data + data_str
            if not data:
                # disconnect
                print("Client Disconnect")
                all_data = ''
                break
            # print(all_data)
            # client send full text
            if all_data[-1] is '\0':
                # cut end char
                api_name = all_data[0:-1]
                print("receive api request:" + api_name)
                resp = server.RequestHandler.handleRequest(api_name)
                client_writer.write(bytes(resp, encoding='utf-8'))
                client_writer.close()
                all_data = ''



            # if prefix is 0 , this socket is likes http (wait to connection closed)
            # if prefix is 1 , this socket is stream




                # client_writer.close()
            # client_writer.write(data)
    pass
