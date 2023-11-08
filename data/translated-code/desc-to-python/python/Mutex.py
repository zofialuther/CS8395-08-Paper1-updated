```python
import threading
import time

max_resources = 2
semaphore = threading.Semaphore(max_resources)

class WorkerThread(threading.Thread):
    def run(self):
        with semaphore:
            print(f"{self.name} acquired a resource")
            time.sleep(2)
            print(f"{self.name} released a resource")

for _ in range(4):
    t = WorkerThread()
    t.start()
```