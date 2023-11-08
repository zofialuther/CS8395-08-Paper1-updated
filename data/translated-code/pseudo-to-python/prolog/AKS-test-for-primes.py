def isPrime(p):
    coefficients = calculateCoefficients(p)
    Cs = coefficients[1:]
    for C in Cs:
        if C % p != 0:
            return False
    return True

def calculateCoefficients(p):
    # implementation of AKS test for calculating coefficients
    # returns list of coefficients for p
    return coefficients

# main program
p = int(input("Enter a number: "))
if isPrime(p):
    print("p is prime")
else:
    print("p is not prime")