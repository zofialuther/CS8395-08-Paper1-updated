import sys
import time
import concurrent.futures

def sleep_sort(nums):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(sleep_and_print, num) for num in nums]

def sleep_and_print(num):
    time.sleep(num * 0.0001)
    print(num)

if __name__ == "__main__":
    nums = [int(num) for num in sys.argv[1:]]
    sleep_sort(nums)