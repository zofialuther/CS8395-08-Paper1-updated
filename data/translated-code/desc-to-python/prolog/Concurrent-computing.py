import threading
import time
import random

def print_message(message):
    delay = random.randint(1, 5)
    time.sleep(delay)
    print(message)

thread1 = threading.Thread(target=print_message, args=("Enjoy",))
thread2 = threading.Thread(target=print_message, args=("Rosetta",))
thread3 = threading.Thread(target=print_message, args=("Code",))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()