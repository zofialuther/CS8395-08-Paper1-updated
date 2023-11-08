def digSum(base, n):
    sum = 0
    while n != 0:
        pair = (n % base, n // base)
        sum = sum + pair[0]
        n = pair[1]
    return sum

def digRoot(base, n):
    sum = digSum(base, n)
    while sum >= base:
        n = n + 1
        sum = digSum(base, n)
    return (n, sum)

def main():
    print("in base 10:")
    numbers = [627615, 39390, 588225, 393900588225]
    for number in numbers:
        result = digRoot(10, number)
        print(number, result)