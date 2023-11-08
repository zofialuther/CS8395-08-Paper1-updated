```python
from threading import Thread, Barrier
import time

class Threads:
    class DelayedMessagePrinter:
        def __init__(self, message, delay, barrier):
            self.message = message
            self.delay = delay
            self.barrier = barrier

        def run(self):
            time.sleep(self.delay)
            print(self.message)
            self.barrier.wait()

    if __name__ == "__main__":
        barrier = Barrier(3)
        thread1 = Thread(target=DelayedMessagePrinter("Message 1", 2, barrier).run)
        thread2 = Thread(target=DelayedMessagePrinter("Message 2", 3, barrier).run)
        thread3 = Thread(target=DelayedMessagePrinter("Message 3", 4, barrier).run)

        thread1.start()
        thread2.start()
        thread3.start()

        thread1.join()
        thread2.join()
        thread3.join()
```