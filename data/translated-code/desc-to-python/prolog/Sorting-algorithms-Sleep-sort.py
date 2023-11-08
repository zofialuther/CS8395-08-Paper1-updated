import time
import concurrent.futures

def sleep_sort(arr):
    def initsort(x):
        time.sleep(x)
        print(x)
        
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(initsort, arr)