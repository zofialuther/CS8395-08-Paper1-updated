def powers2_multiples(dividend, divisor):
    result = 1
    while (divisor * result) <= dividend:
        result = result * 2
    return result / 2

def accumulate(dividend, divisor, quotient):
    return dividend - (divisor * quotient)

def egyptian_divide(dividend, divisor):
    quotient = 0
    remainder = dividend
    while remainder >= divisor:
        multiple = powers2_multiples(remainder, divisor)
        quotient = quotient + multiple
        remainder = accumulate(remainder, divisor, multiple)
    return (quotient, remainder)

def test_egyptian_divide():
    dividend = 580
    divisor = 34
    quotient, remainder = egyptian_divide(dividend, divisor)
    print("Quotient:", quotient)
    print("Remainder:", remainder)

test_egyptian_divide()