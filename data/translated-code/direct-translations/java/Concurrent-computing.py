from threading import Thread, Barrier

class DelayedMessagePrinter:
    def __init__(self, barrier, msg):
        self.barrier = barrier
        self.msg = msg

    def run(self):
        self.barrier.wait()
        print(self.msg)

if __name__ == "__main__":
    barrier = Barrier(3)
    Thread(target=DelayedMessagePrinter(barrier, "Enjoy").run).start()
    Thread(target=DelayedMessagePrinter(barrier, "Rosetta").run).start()
    Thread(target=DelayedMessagePrinter(barrier, "Code").run).start()