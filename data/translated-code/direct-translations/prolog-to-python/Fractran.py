```python
import re

def load(Program, Fractions):
    Split = re.split("[ ]+", Program)
    TextualFractions = odd_items(Split)
    Fractions = list(map(convert_frac, TextualFractions))

def odd_items(L):
    if len(L) == 1:
        return L
    else:
        return [L[i] for i in range(0, len(L), 2)]

def convert_frac(Text):
    match = re.match("([0-9]+)/([0-9]+)", Text)
    return int(match.group(1)) / int(match.group(2))

def step(N, Fs):
    if not Fs:
        return "stop"
    else:
        A = N * Fs[0]
        if isinstance(A, int):
            return A
        else:
            return step(N, Fs[1:])

def exec(Prg, Start):
    Lz = []
    transition(Prg, Start, Lz)

def transition(Prg, N0, N1):
    N1 = step(N0, Prg)

def steps(K, Start, Prg, Seq):
    Values = exec(Prg, Start)
    Seq = [Start] + Values[:K]

def primegen(Prg):
    load("17/91 78/85 19/51 23/38 29/33 77/29 95/23 77/19 1/17 11/13 13/11 15/14 15/2 55/1", Prg)

def primes(N, Primes):
    Prg = primegen(Prg)
    Steps = exec(Prg, 2)
    Primes = [lsb(Q) for Q in Steps if pow2(Q)]

def capture_primes(Ps, Qs):
    if not Qs:
        return
    elif pow2(Qs[0]):
        Ps.append(lsb(Qs[0]))
        capture_primes(Ps, Qs[1:])
    else:
        capture_primes(Ps, Qs[1:])

def pow2(X):
    return X & (X-1) == 0

def main():
    Prg = primegen(Prg)
    Steps = steps(15, 2, Prg, [])
    print("The first 15 steps from PRIMEGEN are:", Steps)
    Primes = primes(20, [])
    print("By running PRIMEGEN we found these primes:", Primes)

main()
```