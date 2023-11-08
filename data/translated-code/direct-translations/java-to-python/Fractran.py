from typing import List
import re

class Fractran:
    def __init__(self, prog: str, val: int):
        self.limit = 15
        self.num = []
        self.den = []
        self.compile(prog)
        self.dump()
        self.exec(val)

    def compile(self, prog: str):
        regexp = re.compile(r'\s*(\d*)\s*\/\s*(\d*)\s*(.*)')
        matches = re.findall(regexp, prog)
        for match in matches:
            self.num.append(int(match[0]))
            self.den.append(int(match[1]))

    def exec(self, val: int):
        n = 0
        while val is not None and n < self.limit:
            print(f'{n}: {val}')
            val = self.step(val)
            n += 1

    def step(self, val: int) -> int:
        i = 0
        while i < len(self.den) and val % self.den[i] != 0:
            i += 1
        if i < len(self.den):
            return self.num[i] * val // self.den[i]
        return None

    def dump(self):
        for i in range(len(self.den)):
            print(f'{self.num[i]}/{self.den[i]} ', end='')
        print()

Fractran("17/91 78/85 19/51 23/38 29/33 77/29 95/23 77/19 1/17 11/13 13/11 15/14 15/2 55/1", 2)