```python
import threading

class VolatileClass:
    def __init__(self):
        self.mutex = threading.Semaphore(1)

    def synchronized_method(self):
        with self.mutex:
            # code for synchronized method

    def acquire_mutex(self):
        self.mutex.acquire()

    def release_mutex(self):
        self.mutex.release()
```