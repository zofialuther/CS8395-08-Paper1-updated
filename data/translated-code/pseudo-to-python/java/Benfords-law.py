def generateFibonacci(n):
    fib = [0] * n
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 2] + fib[i - 1]
    return fib

def main(args):
    numbers = generateFibonacci(1000)
    firstDigits = [0] * 10
    for number in numbers:
        firstDigits[int(str(number)[0])] += 1
    
    for i in range(1, 10):
        print(i, float(firstDigits[i] / len(numbers)), math.log10(1.0 + 1.0 / i))