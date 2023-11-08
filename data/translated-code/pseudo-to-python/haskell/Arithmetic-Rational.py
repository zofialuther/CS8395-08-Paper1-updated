from Data.Ratio import *

def main():
    N = 4
    perfect_numbers = [n for n in range(2, 10000) if getSum(n) == n]
    mapM_(print, take(N, perfect_numbers))

def getSum(candidate):
    factors_sum = 1 % candidate
    for factor in range(2, int(candidate ** 0.5) + 1):
        if candidate % factor == 0:
            factors_sum += 1 % factor + 1 % (candidate // factor)
    return factors_sum