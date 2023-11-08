def MULTIPLY(x, y):
    return x * y

class num(float):
    def __pow__(self, b):
        return reduce(MULTIPLY, [self]*b, 1)

# works with ints as function or operator
print(num(2).__pow__(3))
print(num(2) ** 3)

# works with floats as function or operator
print(num(2.3).__pow__(8))
print(num(2.3) ** 8)