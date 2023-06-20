from rpc import RPCClient

server = RPCClient('0.0.0.0', 8080)

server.connect()

print(server.add(5, 6))
print(server.sub(5, 6))

server.disconnect()