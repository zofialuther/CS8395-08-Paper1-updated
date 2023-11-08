from threading import Thread
from threading import Barrier

class Threads:
    class DelayedMessagePrinter:
        def __init__(self, barrier, msg):
            self.barrier = barrier
            self.msg = msg
        
        def run(self):
            try:
                self.barrier.wait()
            except Exception as e:
                print(self.msg)

    def main(args):
        barrier = Barrier(3)
        t1 = Thread(target=Threads.DelayedMessagePrinter(barrier, "Enjoy").run)
        t2 = Thread(target=Threads.DelayedMessagePrinter(barrier, "Rosetta").run)
        t3 = Thread(target=Threads.DelayedMessagePrinter(barrier, "Code").run)
        t1.start()
        t2.start()
        t3.start()

Threads.main([])