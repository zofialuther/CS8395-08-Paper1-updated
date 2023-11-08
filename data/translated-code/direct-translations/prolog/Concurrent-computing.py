import threading
import time
import random

def say(message):
    delay = random.random()
    time.sleep(delay)
    print(message)

def main():
    a = threading.Thread(target=say, args=("Enjoy",))
    b = threading.Thread(target=say, args=("Rosetta",))
    c = threading.Thread(target=say, args=("Code",))
    a.start()
    b.start()
    c.start()
    a.join()
    b.join()
    c.join()

if __name__ == "__main__":
    main()