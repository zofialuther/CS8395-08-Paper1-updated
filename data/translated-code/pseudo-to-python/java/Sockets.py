import socket

class SocketSend:
    def main():
        sendData("localhost", "hello socket world")

    def sendData(host, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, 256))
        s.sendall(msg.encode('utf-8'))
        s.close()

if __name__ == "__main__":
    SocketSend.main()