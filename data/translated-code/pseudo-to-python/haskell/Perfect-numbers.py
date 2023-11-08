def isPerfect(n):
    lows = list(filter(lambda x: n % x == 0, range(1, int(n**0.5) + 1)))
    return n > 1 and n == sum(lows + [n//x for x in lows if x != n//x]) // 2

def main():
    print(list(filter(isPerfect, range(1, 10001)))