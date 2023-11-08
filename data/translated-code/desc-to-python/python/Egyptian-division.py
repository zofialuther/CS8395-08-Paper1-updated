```python
def egyptian_divmod(dividend, divisor):
    powers = []
    doubles = []
    remainder = dividend
    while remainder >= divisor:
        power = 1
        double = divisor
        while double <= remainder:
            power *= 2
            double *= 2
        powers.append(power)
        doubles.append(double // 2)
        remainder -= double // 2
    quotient = sum(powers)
    return quotient, dividend - quotient * divisor

# Test the custom function
print(egyptian_divmod(580, 34))
print(divmod(580, 34))

# Use the custom function to divide 580 by 34
result = egyptian_divmod(580, 34)
print(f"The quotient is {result[0]} and the remainder is {result[1]}.")
```