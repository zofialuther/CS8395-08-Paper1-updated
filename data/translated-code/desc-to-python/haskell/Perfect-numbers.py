def isPerfect(num):
    factors = [1]
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            factors.append(i)
    return sum(factors) == num

def main():
    perfect_numbers = [num for num in range(1, 10001) if isPerfect(num)]
    print(perfect_numbers)

main()