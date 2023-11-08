```python
def divide_egyptian(num, den):
    powers = []
    doubles = []
    result = 0
    
    while den <= num:
        powers.append(den)
        doubles.append(1)
        den *= 2
    
    for i in range(len(powers) - 1, -1, -1):
        if powers[i] <= num:
            num -= powers[i]
            result += doubles[i]

    return result, num


def main():
    num = 580
    den = 34
    result, remainder = divide_egyptian(num, den)
    print(f"The result is {result} with a remainder of {remainder}")


main()
```