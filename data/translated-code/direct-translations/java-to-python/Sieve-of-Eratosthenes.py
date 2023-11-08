from queue import PriorityQueue
from typing import Iterator
from math import isqrt

class InfiniteSieve(Iterator[int]):
    class NonPrimeSequence:
        def __init__(self, p: int):
            self.currentMultiple = p * p
            self.prime = p

        def __lt__(self, other):
            return self.currentMultiple < other.currentMultiple

    def __init__(self):
        self.i = 2
        self.nonprimes = PriorityQueue()

    def has_next(self):
        return True

    def next(self):
        while not self.nonprimes.empty() and self.i == self.nonprimes.queue[0].currentMultiple:
            while self.nonprimes.queue[0].currentMultiple == self.i:
                x = self.nonprimes.get()
                x.currentMultiple += x.prime
                self.nonprimes.put(x)
            self.i += 1
        self.nonprimes.put(self.NonPrimeSequence(self.i))
        result = self.i
        self.i += 1
        return result

if __name__ == "__main__":
    sieve = InfiniteSieve()
    for i in range(25):
        print(sieve.next())