import socket

def sendData(host, msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, 256))
    sock.sendall(msg.encode())
    sock.close()

sendData("localhost", "hello socket world")