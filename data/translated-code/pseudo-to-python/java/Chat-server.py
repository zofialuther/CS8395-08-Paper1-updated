```python
import socket
import threading
import traceback

class ChatServer:
    def __init__(self, port):
        self.port = port
        self.clients = []

    def run(self):
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(('', self.port))
            server_socket.listen(5)
            print("Server is running on port", self.port)
            while True:
                client_socket, address = server_socket.accept()
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
        except Exception as e:
            traceback.print_exc()

    def register_client(self, client):
        for c in self.clients:
            if c.clientName == client.clientName:
                return False
        self.clients.append(client)
        return True

    def deregister_client(self, client):
        was_registered = False
        with threading.Lock():
            if client in self.clients:
                self.clients.remove(client)
                was_registered = True
        if was_registered:
            self.broadcast(client, " has left the chat")

    def get_online_list_csv(self):
        online_list = "Number of clients online: " + str(len(self.clients)) + " user(s) online: "
        for c in self.clients:
            online_list += c.clientName + ", "
        return online_list

    def broadcast(self, from_client, msg):
        with threading.Lock():
            for c in self.clients:
                if c != from_client:
                    try:
                        c.write(msg)
                    except:
                        pass

class Client:
    def __init__(self, socket):
        self.socket = socket
        self.output = socket.makefile('w')
        self.clientName = None

    def run(self):
        try:
            self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096)
            self.output.write("Please enter your name: ")
            self.output.flush()
            self.clientName = self.socket.recv(1024).decode().strip()
            if not self.clientName:
                self.output.write("Name cannot be empty. Please enter your name again: ")
                self.output.flush()
                self.clientName = self.socket.recv(1024).decode().strip()
            if not chat_server.register_client(self):
                self.output.write("Name already in use. Please enter your name again: ")
                self.output.flush()
                self.clientName = self.socket.recv(1024).decode().strip()
                chat_server.register_client(self)
            self.output.write(chat_server.get_online_list_csv())
            self.output.flush()
            chat_server.broadcast(self, " has joined the chat")
            while True:
                msg = self.socket.recv(1024).decode()
                if msg == "/quit":
                    return
                chat_server.broadcast(self, self.clientName + ": " + msg)
        except:
            pass
        finally:
            chat_server.deregister_client(self)
            self.output = None
            self.socket.close()

    def write(self, msg):
        self.output.write(msg)
        self.output.flush()

    def __eq__(self, other):
        return self.clientName == other.clientName

def main():
    default_port = 4004
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = default_port
    chat_server = ChatServer(port)
    chat_server.run()

if __name__ == "__main__":
    main()
```