from threading import Thread
import time

class SleepSort:
    @staticmethod
    def sleepSortAndPrint(arr):
        doneSignal = len(arr)

        def run(val):
            nonlocal doneSignal
            time.sleep(val)
            print(val)
            doneSignal -= 1

        for num in arr:
            Thread(target=run, args=(num,)).start()
        
        while doneSignal > 0:
            time.sleep(1)

if __name__ == "__main__":
    import sys
    input_arr = [int(x) for x in sys.argv[1:]]
    SleepSort.sleepSortAndPrint(input_arr)