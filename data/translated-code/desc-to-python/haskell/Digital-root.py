def digSum(base, number):
    return sum(int(digit, base=base) for digit in str(number))

def digRoot(base, number):
    while number >= base:
        number = digSum(base, number)
    return (number, number)

def main():
    numbers = [123, 456, 789]
    for number in numbers:
        root, original = digRoot(10, number)
        print(f"The digital root of {original} in base 10 is {root}")

main()