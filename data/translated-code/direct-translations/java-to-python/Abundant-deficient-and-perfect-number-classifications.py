def properDivsSum(n):
    return sum(i for i in range(1, (n + 1) // 2 + 1) if n % i == 0)

def main():
    deficient = 0
    perfect = 0
    abundant = 0

    for i in range(1, 20001):
        sum = properDivsSum(i)
        if sum < i:
            deficient += 1
        elif sum == i:
            perfect += 1
        else:
            abundant += 1

    print("Deficient:", deficient)
    print("Perfect:", perfect)
    print("Abundant:", abundant)

if __name__ == "__main__":
    main()