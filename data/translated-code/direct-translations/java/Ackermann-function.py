```python
import os
import threading
import math
import sys
from collections import deque

class IterativeAckermannMemoryOptimization(threading.Thread):
    SYSTEM_MEMORY_LIMIT_PERCENTAGE = 0.1

    def __init__(self, iterativeAckermann):
        super().__init__()
        self.iterativeAckermann = iterativeAckermann

    def getIterativeAckermann(self):
        return self.iterativeAckermann

    def setIterativeAckermann(self, iterativeAckermann):
        self.iterativeAckermann = iterativeAckermann

    @staticmethod
    def getSystemMemoryLimitPercentage():
        return IterativeAckermannMemoryOptimization.SYSTEM_MEMORY_LIMIT_PERCENTAGE

    def run(self):
        operating_system = os.name
        if operating_system == "nt" or operating_system == "posix" or operating_system == "mac":
            IterativeAckermannMemoryOptimization.SYSTEM_MEMORY_LIMIT_PERCENTAGE = 0.25

        while self.iterativeAckermann.getConsumed_heap() >= IterativeAckermannMemoryOptimization.SYSTEM_MEMORY_LIMIT_PERCENTAGE * sys.getsizeof(0):
            try:
                threading.Event().wait()
            except Exception as e:
                print(e)

        if not self.iterativeAckermann.is_alive():
            self.iterativeAckermann.start()
        else:
            threading.Event().set()

class IterativeAckermann(threading.Thread):
    HASH_SIZE_LIMIT = 636
    LIMIT = 6

    def __init__(self, m, n, invalid, invalid2):
        super().__init__()
        self.m = m
        self.n = n
        self.hash_size = invalid
        self.consumed_heap = invalid2

    def run(self):
        while self.hash_size >= IterativeAckermann.HASH_SIZE_LIMIT:
            try:
                threading.Event().wait()
            except Exception as e:
                print(e)

        for i in range(0, IterativeAckermann.LIMIT):
            for j in range(0, IterativeAckermann.LIMIT):
                iterativeAckermann = IterativeAckermann(i, j, None, None)
                print("Ackmermann({}, {}) = {}".format(i, j, iterativeAckermann.iterative_ackermann(i, j)))

    def getM(self):
        return self.m

    def setM(self, m):
        self.m = m

    def getN(self):
        return self.n

    def setN(self, n):
        self.n = n

    def getHash_size(self):
        return self.hash_size

    def setHash_size(self, hash_size):
        self.hash_size = hash_size

    def getConsumed_heap(self):
        return self.consumed_heap

    def setConsumed_heap(self, consumed_heap):
        self.consumed_heap = consumed_heap

    def iterative_ackermann(self, m, n):
        if m >= 0 and n >= 0:
            solved_set = {}
            to_solve = deque()
            to_solve.append((m, n))

            while to_solve:
                head = to_solve[-1]
                if head[0] == 0:
                    solved_set[head] = head[1] + 1
                    to_solve.pop()
                elif head[1] == 0:
                    next0 = (head[0] - 1, 1)
                    result0 = solved_set.get(next0)
                    if result0 is None:
                        to_solve.append(next0)
                    else:
                        solved_set[head] = result0
                        to_solve.pop()
                else:
                    next0 = (head[0], head[1] - 1)
                    result0 = solved_set.get(next0)
                    if result0 is None:
                        to_solve.append(next0)
                    else:
                        next1 = (head[0] - 1, result0)
                        result1 = solved_set.get(next1)
                        if result1 is None:
                            to_solve.append(next1)
                        else:
                            solved_set[head] = result1
                            to_solve.pop()

            self.hash_size = len(solved_set)
            print("Hash Size:", self.hash_size)
            self.consumed_heap = math.ceil(sys.getsizeof(solved_set) / (1024 * 1024))
            print("Consumed Heap:", self.consumed_heap, "m")
            self.setHash_size(self.hash_size)
            self.setConsumed_heap(self.consumed_heap)
            return solved_set[(m, n)]

        raise ValueError("The arguments must be non-negative integers.")

if __name__ == "__main__":
    iterative_ackermann_memory_optimization = IterativeAckermannMemoryOptimization(IterativeAckermann(None, None, 0, 0))
    iterative_ackermann_memory_optimization.start()
```