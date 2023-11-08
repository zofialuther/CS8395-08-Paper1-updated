import sympy

primes1e6 = list(filter(lambda x: '0' not in str(x), reversed(list(sympy.primerange(0, 1000000))))

def rightT(num):
    while num > 0:
        if num not in primes1e6:
            return False
        num = num // 10
    return True

def leftT(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if int(num_str[i:]) not in primes1e6:
            return False
    return True

def main():
    for num in primes1e6:
        if rightT(num) and leftT(num):
            print(num)
            return

main()