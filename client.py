from rpc import RPCClient

server = RPCClient('localhost', 8080)

server.connect()

print(server.add(5, 6))
print(server.sub(5, 6))

server.disconnect()