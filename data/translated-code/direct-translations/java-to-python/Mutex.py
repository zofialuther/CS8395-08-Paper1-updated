from threading import Semaphore

class VolatileClass:
    def __init__(self):
        self.mutex = Semaphore(1)

    def needsToBeSynched(self):
        #...