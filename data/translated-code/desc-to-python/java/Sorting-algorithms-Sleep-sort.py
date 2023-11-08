```python
import threading
import time

def sleep_sort_and_print(arr):
    result = []

    def helper(x):
        time.sleep(x)
        result.append(x)

    threads = [threading.Thread(target=helper, args=(x,)) for x in arr]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(result)

if __name__ == "__main__":
    import sys
    input_arr = [int(x) for x in sys.argv[1:]]
    sleep_sort_and_print(input_arr)
```