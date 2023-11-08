from threading import Semaphore

class VolatileClass:
    def __init__(self):
        self.mutex = Semaphore(1)

    def needsToBeSynched(self):
        pass

    def acquireMutex(self):
        self.mutex.acquire()

    def releaseMutex(self):
        self.mutex.release()