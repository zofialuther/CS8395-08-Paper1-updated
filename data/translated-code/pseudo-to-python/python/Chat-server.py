import socket
import time
import _thread as thread

HOST = '127.0.0.1'  # Replace with your server's IP address
PORT = 65432        # Port to listen on

# Set up the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("Listening on %s" % ("%s:%s" % server.getsockname()))

# Main event loop
users = {}
while True:
    try:
        # Accept new connections
        while True:
            try:
                conn, addr = server.accept()
            except socket.error:
                break
            accept(conn)

        # Read from connections
        for name, conn in users.items():
            try:
                message = conn.recv(1024)
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

# Accept func
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
    thread.start_new_thread(threaded, ())

# Broadcast func
def broadcast(name, message):
    print(message)
    for to_name, conn in users.items():
        if to_name != name:
            try:
                conn.send((message + "\n").encode())
            except socket.error:
                pass