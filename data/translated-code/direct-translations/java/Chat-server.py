```python
import socket
import threading

class ChatServer:
    def __init__(self, port):
        self.port = port
        self.clients = []

    def run(self):
        try:
            ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ss.bind(('localhost', self.port))
            ss.listen(5)
            print("Server is running on port", self.port)
            while True:
                s, addr = ss.accept()
                new_client = Client(s, self)
                self.clients.append(new_client)
                new_client.start()
        except Exception as e:
            print(e)

    def register_client(self, client):
        for other_client in self.clients:
            if other_client.client_name.lower() == client.client_name.lower():
                return False
        self.clients.append(client)
        return True

    def deregister_client(self, client):
        if client in self.clients:
            self.clients.remove(client)
            self.broadcast(client, f"--- {client.client_name} left ---")

    def get_online_list_csv(self):
        online_list = [client.client_name for client in self.clients]
        return f"{len(online_list)} user(s) online: {', '.join(online_list)}"

    def broadcast(self, from_client, msg):
        for client in self.clients:
            if client != from_client:
                try:
                    client.send(msg.encode())
                except Exception as e:
                    print(e)

class Client(threading.Thread):
    def __init__(self, socket, server):
        threading.Thread.__init__(self)
        self.socket = socket
        self.server = server
        self.client_name = None

    def run(self):
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 16384)
            self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            self.input = self.socket.makefile('r')
            self.output = self.socket.makefile('w')
            self.write("Please enter your name: ")
            while True:
                line = self.input.readline().strip()
                if not line:
                    continue
                if self.client_name is None:
                    if not line:
                        self.write("A name is required. Please enter your name: ")
                        continue
                    self.client_name = line
                    if not self.server.register_client(self):
                        self.client_name = None
                        self.write("Name already registered. Please enter your name: ")
                        continue
                    self.write(self.server.get_online_list_csv() + "\r\n")
                    self.server.broadcast(self, f"+++ {self.client_name} arrived +++")
                    continue
                if line.lower() == "/quit":
                    return
                self.server.broadcast(self, f"{self.client_name}> {line}")
        except Exception as e:
            print(e)
        finally:
            self.server.deregister_client(self)
            self.output = None
            self.socket.close()

    def write(self, msg):
        self.output.write(msg)
        self.output.flush()

if __name__ == "__main__":
    port = 4004
    chat_server = ChatServer(port)
    chat_server.run()
```