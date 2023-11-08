import time
import threading
import sys

def sleep_sort(num):
    def sleep_and_print(n):
        time.sleep(n)
        print(n)

    threads = [threading.Thread(target=sleep_and_print, args=(n,)) for n in num]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    numbers = [int(x) for x in sys.argv[1:]]
    sleep_sort(numbers)