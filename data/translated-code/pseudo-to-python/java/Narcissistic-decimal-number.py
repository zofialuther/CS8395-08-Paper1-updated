import math

numbersToCalculate = 25
numbersCalculated = 0

def main():
    for i in range(0, math.inf):
        num_str = str(i)
        length = len(num_str)
        addedDigits = 0

        for digit in num_str:
            digit_val = int(digit)
            addedDigits += digit_val ** length

        if i == addedDigits:
            numbersCalculated += 1
            print(addedDigits)

        if numbersCalculated == numbersToCalculate:
            break

main()