```python
import socket
import _thread
import time

HOST = ""
PORT = 4004
users = {}

def accept(conn):
    def threaded():
        while True:
            conn.send(b"Please enter your name: ")
            try:
                name = conn.recv(1024).strip()
            except socket.error:
                continue
            if name in users:
                conn.send(b"Name entered is already in use.\n")
            elif name:
                conn.setblocking(False)
                users[name] = conn
                broadcast(name, "+++ %s arrived +++" % name)
                break
    _thread.start_new_thread(threaded, ())

def broadcast(name, message):
    print(message)
    for to_name, conn in users.items():
        if to_name != name:
            try:
                conn.send(bytes(message + "\n", "utf-8"))
            except socket.error:
                pass

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setblocking(False)
server.bind((HOST, PORT))
server.listen(1)
print("Listening on %s" % ("%s:%s" % server.getsockname()))

while True:
    try:
        while True:
            try:
                conn, addr = server.accept()
            except socket.error:
                break
            accept(conn)
        for name, conn in list(users.items()):
            try:
                message = conn.recv(1024).decode("utf-8")
            except socket.error:
                continue
            if not message:
                del users[name]
                broadcast(name, "--- %s leaves ---" % name)
            else:
                broadcast(name, "%s> %s" % (name, message.strip()))
        time.sleep(.1)
    except (SystemExit, KeyboardInterrupt):
        break
```