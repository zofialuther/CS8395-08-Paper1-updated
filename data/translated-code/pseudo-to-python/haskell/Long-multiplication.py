def longmult(x, y):
    digitsX = digits(x)
    digitsY = digits(y)
    products = polymul(digitsX, digitsY)
    result = functools.reduce(lambda x, y: x + y * 10, products)
    return result

def polymul(xs, ys):
    zeros = list(itertools.accumulate(itertools.repeat(0), initial=0))
    zipped = list(map(list, zip(zeros, map(lambda x, y: list(map(lambda f: f * x, y)), xs, itertools.repeat(ys))))
    transposed = list(map(sum, zip(*zipped)))
    result = sum(transposed)
    return result

def digits(num):
    strNum = str(num)
    result = [int(digit) for digit in strNum]
    return result

def main():
    result = longmult(2 ** 64, 2 ** 64)
    print(result)