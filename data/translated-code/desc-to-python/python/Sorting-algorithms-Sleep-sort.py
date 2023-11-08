```python
import time
import threading

def sleepsort(values):
    result = []

    def add_result(value):
        time.sleep(value)
        result.append(value)

    max_value = max(values)
    threads = [threading.Thread(target=add_result, args=(value,)) for value in values]
    for thread in threads:
        thread.start()
    time.sleep(max_value + 1)
    return result

# Test the sleepsort function
input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(sleepsort(input_list))  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```