from threading import Thread
from time import sleep

def sleep_sort_and_print(nums):
    done_signal = CountDownLatch(len(nums))
    for num in nums:
        def sleeper(num):
            done_signal.countDown()
            done_signal.await()
            sleep(num)
            print(num)

        t = Thread(target=sleeper, args=(num,))
        t.start()

if __name__ == "__main__":
    import sys
    nums = [int(num) for num in sys.argv[1:]]
    sleep_sort_and_print(nums)