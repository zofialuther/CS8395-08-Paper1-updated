def eApprox(n):
    e = 1
    factorial = 1
    for i in range(1, n):
        factorial *= i
        e += 1 / factorial
    return e

def main():
    result = eApprox(20)
    print(result)

main()