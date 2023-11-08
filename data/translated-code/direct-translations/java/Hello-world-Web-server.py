import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)

    while True:
        client_socket, addr = server_socket.accept()
        print("Got a connection from", addr)
        client_socket.sendall(b"Goodbye, World!")
        client_socket.close()

if __name__ == "__main__":
    main()