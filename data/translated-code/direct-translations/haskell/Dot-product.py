def dotp(a, b):
    if len(a) == len(b):
        return sum([x*y for x, y in zip(a, b)])
    else:
        raise ValueError("Vector sizes must match")

print(dotp([1, 3, -5], [4, -2, -1])) # prints 3