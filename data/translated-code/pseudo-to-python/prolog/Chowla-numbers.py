def chowla(N, C):
    if N == 1 or N == 2:
        return 0
    else:
        Max = int(N ** 0.5)
        Xs = [X for X in range(2, Max+1) if N % X == 0]
        Ys = [N // X1 for X1 in Xs if N // X1 != Max]
        S1 = sum(Xs)
        S2 = sum(Ys)
        C = S1 + S2
        return C

def prime_count(Upper, Count):
    return Count if Upper == Count else prime_count(Upper, Count+1) if chowla(Count, 0) else prime_count(Upper, Count+1)

def perfect_numbers(Upper, AccNums):
    return AccNums[::-1] if Upper == AccNums else perfect_numbers(Upper, [Lower] + AccNums) if chowla(Lower, Lower - 1) else perfect_numbers(Upper, AccNums)

def main():
    for N in range(1, 38):
        C = chowla(N, 0)
        print(f'chowla({N}) = {C}')
    
    Ranges = [100, 1000, 10000, 100000, 1000000, 10000000]
    for Range in Ranges:
        PrimeCount = prime_count(Range, 2)
        print(f'There are {PrimeCount} primes less than {Range}.')
    
    Limit = 35000000
    Nums = perfect_numbers(2, [])
    for Perfect in Nums:
        print(f'{Perfect} is a perfect number.')
    PerfectCount = len(Nums)
    print(f'There are {PerfectCount} perfect numbers < {Limit}.')

main()