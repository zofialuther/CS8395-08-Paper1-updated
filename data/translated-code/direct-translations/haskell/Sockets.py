import socket

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"hello socket world", ("localhost", 256))

if __name__ == "__main__":
    main()