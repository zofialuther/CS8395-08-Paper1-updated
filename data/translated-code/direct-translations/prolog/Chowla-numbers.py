def chowla(N, C):
    if N == 1 or N == 2:
        C = 0
    else:
        Max = int(N ** 0.5)
        Xs = [X for X in range(2, Max + 1) if N % X == 0]
        Ys = [N // X1 for X1 in Xs if N // X1 != Max]
        S1 = sum(Xs)
        S2 = sum(Ys)
        C = S1 + S2
    return C

def prime_count(Lower, Upper, Add, Count):
    if Lower == Upper:
        return Count
    if chowla(Lower, 0) != 0:
        Lower += 1
        Add += 1
    return prime_count(Lower + 1, Upper, Add, Count)

def perfect_numbers(Lower, Upper, AccNums):
    if Lower == Upper:
        return AccNums
    Perfect = Lower - 1
    if chowla(Lower, Perfect) == 0:
        AccNums.append(Lower)
    return perfect_numbers(Lower + 1, Upper, AccNums)

def main():
    for N in range(1, 38):
        C = chowla(N, 0)
        print(f"chowla({N}) = {C}")

    Ranges = [100, 1000, 10000, 100000, 1000000, 10000000]
    for Range in Ranges:
        PrimeCount = prime_count(2, Range, 0, 0)
        print(f"There are {PrimeCount} primes less than {Range}.")

    Limit = 35000000
    Nums = perfect_numbers(2, Limit, [])
    for Perfect in Nums:
        print(f"{Perfect} is a perfect number.")
    PerfectCount = len(Nums)
    print(f"There are {PerfectCount} perfect numbers < {Limit}.")

main()