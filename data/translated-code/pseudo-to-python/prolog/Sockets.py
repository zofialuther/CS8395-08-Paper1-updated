import socket

def start(Port):
    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Socket.connect(('localhost', Port))
    Output = Socket.makefile('w')
    Input = Socket.makefile('r')
    Output.write('hello socket world')
    Output.flush()
    Output.close()
    Input.close()