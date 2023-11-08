```python
# Python does not have a direct translation of the given Java code. 
# However, a similar chat server can be implemented using Python's socket and threading modules.
# Below is a basic example of how a simple chat server can be implemented in Python.

import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, client_socket, client_address):
        super(ClientThread, self).__init__()
        self.client_socket = client_socket
        self.client_address = client_address

    def run(self):
        while True:
            message = self.client_socket.recv(1024).decode('utf-8')
            # handle and broadcast the message to all clients

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Chat server is listening on", self.port)

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"New connection from {client_address}")
            client_thread = ClientThread(client_socket, client_address)
            client_thread.start()
            self.clients.append(client_thread)

chat_server = ChatServer('localhost', 12345)
chat_server.start()
```