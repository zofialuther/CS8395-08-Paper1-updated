import threading
import time

res = 2
semaphore = threading.Semaphore(res)

class ResThread(threading.Thread):
    def run(self):
        n = threading.current_thread().name
        for i in range(1, 4):
            semaphore.acquire()
            res -= 1
            print(n, res)
            time.sleep(2)
            res += 1
            print(n, res)
            semaphore.release()

for _ in range(4):
    thread = ResThread()
    thread.start()