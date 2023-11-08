```python
import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish connection to local host on port 256
client_socket.connect(('localhost', 256))

# send message through the socket
client_socket.send(b"hello socket world")

# close the connection
client_socket.close()
```