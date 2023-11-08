import socket

class HelloWorld:
    def main():
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind(('localhost', 8080))
        listener.listen(1)
        while True:
            sock, addr = listener.accept()
            print("Goodbye, World!", file=sock.makefile('w'))
            sock.close()

if __name__ == "__main__":
    HelloWorld.main()