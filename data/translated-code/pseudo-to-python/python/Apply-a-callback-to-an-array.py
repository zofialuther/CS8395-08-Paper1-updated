def square(n):
    return n * n
    
numbers = [1, 3, 5, 7]

squares1 = []
for n in numbers:
    squares1.append(square(n))

squares2a = list(map(square, numbers))

squares2b = list(map(lambda x: x*x, numbers))

squares3 = []
for n in numbers:
    squares3.append(n * n)

isquares1 = (n * n for n in numbers)

import itertools
isquares2 = itertools.imap(square, numbers)