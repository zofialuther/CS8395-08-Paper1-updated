from queue import PriorityQueue
from typing import Iterator
from math import isqrt
from functools import total_ordering

@total_ordering
class NonPrimeSequence:
    def __init__(self, p):
        self.prime = p
        self.currentMultiple = p * p

    def __eq__(self, other):
        return self.currentMultiple == other.currentMultiple

    def __lt__(self, other):
        return self.currentMultiple < other.currentMultiple

class InfiniteSieve(Iterator):
    def __init__(self):
        self.i = 2
        self.nonprimes = PriorityQueue()

    def __iter__(self):
        return self

    def __next__(self):
        while not self.nonprimes.empty() and self.i == self.nonprimes.queue[0].currentMultiple:
            while self.nonprimes.queue[0].currentMultiple == self.i:
                x = self.nonprimes.get()
                x.currentMultiple += x.prime
                self.nonprimes.put(x)
            self.i += 1
        self.nonprimes.put(NonPrimeSequence(self.i))
        result = self.i
        self.i += 1
        return result

def main(args):
    sieve = InfiniteSieve()
    for i in range(25):
        print(next(sieve))