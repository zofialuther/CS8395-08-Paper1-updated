```python
import socket

def sendData(host, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, 12345))
    client_socket.send(message.encode())
    client_socket.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    message = "Hello, server!"
    sendData(host, message)
```