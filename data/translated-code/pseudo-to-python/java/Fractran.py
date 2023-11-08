from typing import List

def main():
    fractran("17/91 78/85 19/51 23/38 29/33 77/29 95/23 77/19 1/17 11/13 13/11 15/14 15/2 55/1", 2)

def fractran(prog: str, limit: int):
    num = []
    den = []
    compile(prog, num, den)
    dump(num, den)
    exec(2, limit)

def compile(prog: str, num: List[int], den: List[int]):
    import re
    regexp = re.compile("\s*(\d*)\s*\/\s*(\d*)\s*(.*)")
    matcher = regexp.match(prog)
    while matcher:
        num.append(int(matcher.group(1)))
        den.append(int(matcher.group(2)))
        matcher = regexp.match(matcher.group(3))

def exec(val: int, limit: int):
    n = 0
    while val is not None and n < limit:
        print(n, val)
        val = step(val)
        n += 1

def step(val: int):
    i = 0
    while i < len(den) and val % den[i] != 0:
        i += 1
    if i < len(den):
        return num[i] * val // den[i]
    else:
        return None

def dump(num: List[int], den: List[int]):
    for i in range(len(den)):
        print(num[i], "/", den[i], " ", end="")
    print("\n")

main()