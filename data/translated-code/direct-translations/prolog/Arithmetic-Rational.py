import math

def divisor(N, Div):
    Max = math.floor(math.sqrt(N))
    for D in range(1, Max+1):
        if N % D == 0:
            if D == N // D:
                Div.append(D)
            else:
                Div.append(D)
                Div.append(N // D)

def divisors(N, Divs):
    Div = []
    divisor(N, Div)
    Divs = list(set(Div))

def recip(A, B):
    B = 1 / A

def sumrecip(N, A):
    Divs = []
    divisors(N, Divs)
    As = [recip(D, A) for D in Divs]
    A = sum(As)

def perfect(X):
    A = 1
    sumrecip(X, A)

def main():
    Limit = 1 << 19
    for N in range(1, Limit+1):
        if perfect(N):
            print(N)

main()