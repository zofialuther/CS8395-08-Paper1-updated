def eApprox(n):
    sum = 0
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
        sum = sum + (1 / factorial)
    return sum

def main():
    result = eApprox(20)
    print(result)

main()