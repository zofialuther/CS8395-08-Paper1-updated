import threading
import time

def sleep_sort(L):
    def initsort(V):
        time.sleep(V)
        print(V)

    for V in L:
        t = threading.Thread(target=initsort, args=(V,))
        t.start()

sleep_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])