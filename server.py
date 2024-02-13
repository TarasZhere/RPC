class Mathematics:
    def add(a, b):
        return a+b

    def sub(a, b):
        return a-b

from rpc import RPCServer

server = RPCServer()

server.registerInstance(Mathematics)

server.run()