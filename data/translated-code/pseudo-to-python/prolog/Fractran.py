import re
from fractions import Fraction

def load(Program, Fractions):
    Split = re.split("[ ]+", Program)
    TextualFractions = odd_items(Split)
    Fractions = list(map(convert_frac, TextualFractions))

def odd_items(L):
    if len(L) == 1:
        return L
    else:
        return L[0::2]

def convert_frac(Text):
    match = re.match("([0-9]+)/([0-9]+)", Text)
    return Fraction(int(match.group(1)), int(match.group(2)))

def step(N, Fs):
    for F in Fs:
        A = N * F
        if isinstance(A, int):
            return A
    return 'stop'

def exec(Prg, Start):
    Lz = [transition(Prg, Start)]
    return Lz

def transition(Prg, N0):
    N1 = step(N0, Prg)
    return N1

def steps(K, Start, Prg):
    Values = exec(Prg, Start)
    Seq = [Start] + Values[:K-1]
    return Seq

def primegen(Prg):
    load("17/91 78/85 19/51 23/38 29/33 77/29 95/23 77/19 1/17 11/13 13/11 15/14 15/2 55/1", Prg)

def primes(N):
    Prg = primegen()
    Steps = exec(Prg, 2)
    Primes = []
    for Q in Steps:
        if pow2(Q):
            Primes.append(lsb(Q))
    return Primes

def pow2(X):
    return X & (X-1) == 0

def main():
    Prg = primegen()
    Steps = steps(15, 2, Prg)
    print("The first 15 steps from PRIMEGEN are:", Steps)
    Primes = primes(20)
    print("By running PRIMEGEN we found these primes:", Primes)

main()