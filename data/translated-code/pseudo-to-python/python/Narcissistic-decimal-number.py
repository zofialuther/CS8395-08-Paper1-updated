from __future__ import print_function
from itertools import count, islice

def narcissists():
    for digits in count(start=0):
        digitpowers = []
        for i in range(0, 10):
            digitpowers.append(i ** digits)
        for n in range(10 ** (digits - 1), 10 ** digits):
            div = n
            digitpsum = 0
            while div != 0:
                div, mod = divmod(div, 10)
                digitpsum += digitpowers[mod]
            if n == digitpsum:
                yield n

for i, n in enumerate(islice(narcissists(), 25)):
    print(n, end=' ')
    if i % 5 == 4:
        print()
print()