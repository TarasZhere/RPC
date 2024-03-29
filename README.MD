# RPC in Python

Very Simple RPCs built with sockets in python.

## Client sample

```python
from rpc import RPCClient

server = RPCClient('localhost', 8080)

server.connect()

print(server.add(5, 6))
print(server.sub(5, 6))

server.disconnect()
```

## Server sample

```python
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

from rpc import RPCServer

server = RPCServer()

server.registerMethod(add)
server.registerMethod(sub)

server.run()
```

## Instance registration

```python
class Mathematics:
    def add(a, b):
        return a+b

    def sub(a, b):
        return a-b

from rpc import RPCServer

server = RPCServer()

server.registerInstance(Mathematics)

server.run()
```
