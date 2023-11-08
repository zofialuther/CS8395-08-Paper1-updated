```python
import socket

def start(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', port))
    s.sendall(b'hello socket world')
    s.shutdown(socket.SHUT_WR)
    s.close()
```