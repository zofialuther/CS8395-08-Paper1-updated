from sympy import isprime, primerange, primefactors

def attractive_numbers():
    return filter(lambda x: isprime(len(primefactors(x))), primerange(1, 121))

def main():
    print(list(attractive_numbers()))

if __name__ == "__main__":
    main()