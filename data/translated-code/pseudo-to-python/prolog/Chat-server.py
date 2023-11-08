```python
import socket
import threading

def chat_server(Port):
    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Socket.bind(('', Port))
    Socket.listen(5)
    while True:
        AcceptFd, _ = Socket.accept()
        dispatch(AcceptFd)

def dispatch(AcceptFd):
    Socket, _ = AcceptFd.accept()
    threading.Thread(target=process_client, args=(Socket,)).start()
    dispatch(AcceptFd)

def process_client(Socket):
    Str = Socket.makefile()
    handle_connection(Str)
    Str.close()

def handle_connection(Str):
    send_msg(Str, msg_welcome)
    while True:
        send_msg(Str, msg_username)
        Name = Str.readline().strip()
        connect_user(Name, Str)

connected = {}

def connect_user(Name, Str):
    if Name in connected:
        send_msg(Str, msg_username_taken)
        return
    else:
        send_msg(Str, msg_welcome_name, Name)
        connected[Name] = Str
        broadcast(msg_joined, Name)
        chat_loop(Name, Str)
        broadcast(msg_left, Name)
        del connected[Name]

def chat_loop(Name, Str):
    S = Str.readline().strip()
    if S:
        broadcast(msg_by_user, Name, S)
        chat_loop(Name, Str)

def broadcast(Msg, *Params):
    for user, user_str in connected.items():
        if user != Params[0]:
            send_msg(user_str, Msg, *Params)

def send_msg(Str, MsgConst, *Params):
    msg = MsgConst.format(*Params)
    Str.write(msg)
    Str.flush()

msg_welcome = 'Welcome to Chatalot\n\r'
msg_username = 'Please enter your nickname: '
msg_welcome_name = 'Welcome ~p\n\r'
msg_joined = ' -- "~w" has joined the chat --'
msg_left = ' -- "~w" has left the chat. --'
msg_username_taken = 'That username is already taken, choose another\n\r'
msg_new_line = '\n\r'
msg_by_user = '~w> ~w'
```