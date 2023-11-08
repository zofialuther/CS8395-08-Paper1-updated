MAX_NUM = 1 << 19
print("Searching for perfect numbers in the range [1, " + str(MAX_NUM - 1) + "]")
TWO = BigRational.valueOf(2)

for i in range(1, MAX_NUM):
    reciprocalSum = BigRational.ONE
    if i > 1:
        reciprocalSum = reciprocalSum + BigRational.valueOf(i).reciprocal()
    
    maxDivisor = i ** 0.5
    if maxDivisor >= i:
        maxDivisor = maxDivisor - 1
    
    for divisor in range(2, int(maxDivisor) + 1):
        if i % divisor == 0:
            reciprocalSum = reciprocalSum + BigRational.valueOf(divisor).reciprocal()
            dividend = i / divisor
            if divisor != dividend:
                reciprocalSum = reciprocalSum + BigRational.valueOf(dividend).reciprocal()
    
    if reciprocalSum.equals(TWO):
        print(str(i) + " is a perfect number")