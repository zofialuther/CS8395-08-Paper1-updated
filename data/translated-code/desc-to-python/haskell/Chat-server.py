import threading

class ClientHandler:
    def __init__(self):
        self.mutex = threading.Lock()
        self.client_set = set()

    def handle_client(self, client):
        with self.mutex:
            self.client_set.add(client)
            # handle client communication

    def main(self):
        while True:
            # accept incoming client connections
            client = self.accept_client()
            client_thread = threading.Thread(target=self.handle_client, args=(client,))
            client_thread.start()