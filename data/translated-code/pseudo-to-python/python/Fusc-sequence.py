def infiniteFusc():
    def go(step):
        a, b = 1, 0
        while True:
            a, b = b, a + b if step % 2 == 0 else b
            step //= 2
            if step == 0:
                yield a
    return map(go, iterate(lambda x: x + 1))

def fusc(i):
    def go(n):
        a, b = 1, 0
        while n > 0:
            a, b = b, a + b if n % 2 == 0 else b
            n //= 2
        return a
    return go(i)

def firstFuscOfEachMagnitude():
    return map(fusc, iterate(lambda x: x * 10))

def main():
    print(list(take(61, infiniteFusc())))
    print(list(firstFuscOfEachMagnitude()))

def iterate(f):
    def gen(x):
        while True:
            yield x
            x = f(x)
    return gen

def showList(xs):
    return "[" + ", ".join(map(str, xs)) + "]"

def take(n, xs):
    result = []
    for _ in range(n):
        try:
            result.append(next(xs))
        except StopIteration:
            break
    return result