```python
import socket
import threading

def chat_server(Port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('', Port))
        server_socket.listen(5)
        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=process_client, args=(conn,)).start()

def process_client(conn):
    with conn:
        handle_connection(conn)

def handle_connection(conn):
    send_msg(conn, msg_welcome, [])
    while True:
        send_msg(conn, msg_username, [])
        name = conn.recv(1024).decode('utf-8')
        if name:
            if connect_user(name, conn):
                break

def connect_user(name, conn):
    if connected(name):
        send_msg(conn, msg_username_taken, [])
        return False
    else:
        send_msg(conn, msg_welcome_name, name)
        connected[name] = conn
        broadcast(name, msg_joined, name)
        chat_loop(name, conn)
        broadcast(name, msg_left, name)
        del connected[name]
        return True

def chat_loop(name, conn):
    while True:
        data = conn.recv(1024).decode('utf-8')
        if data:
            broadcast(name, msg_by_user, [name, data])

def broadcast(name, msg, params):
    for user, user_conn in connected.items():
        if user != name:
            send_msg(user_conn, msg, params)
            send_msg(user_conn, msg_new_line, [])

def send_msg(conn, msg_const, params):
    msg = globals()[msg_const]
    conn.sendall(msg.format(*params).encode('utf-8'))

msg_welcome = 'Welcome to Chatalot\n\r'
msg_username = 'Please enter your nickname: '
msg_welcome_name = 'Welcome {}\n\r'
msg_joined = ' -- "{}" has joined the chat --'
msg_left = ' -- "{}" has left the chat. --'
msg_username_taken = 'That username is already taken, choose another\n\r'
msg_new_line = '\n\r'
msg_by_user = '{}> {}'

connected = {}

if __name__ == "__main__":
    chat_server(5000)
```