import socket

def start(Port):
    Socket = socket.socket(socket.AF_INET)
    Socket.connect(('localhost', Port))
    Input = Socket.makefile('r')
    Output = Socket.makefile('w')
    Output.write('hello socket world')
    Output.flush()
    Output.close()
    Input.close()