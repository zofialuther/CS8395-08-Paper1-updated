import threading
import random
import time

def say(Message):
    Delay = random.random()
    time.sleep(Delay)
    print(Message)

A = threading.Thread(target=say, args=("Enjoy",))
B = threading.Thread(target=say, args=("Rosetta",))
C = threading.Thread(target=say, args=("Code",))

A.start()
B.start()
C.start()

A.join()
B.join()
C.join()