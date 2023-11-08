```python
import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def m_factor(p):
    max_k = 16384 // p
    for k in range(max_k):
        q = 2 * p * k + 1
        if not is_prime(q):
            continue
        elif q % 8 != 1 and q % 8 != 7:
            continue
        elif pow(2, p, q) == 1:
            return q
    return None

if __name__ == '__main__':
    exponent = int(input("Enter exponent of Mersenne number: "))
    if not is_prime(exponent):
        print("Exponent is not prime: %d" % exponent)
    else:
        factor = m_factor(exponent)
        if not factor:
            print("No factor found for M%d" % exponent)
        else:
            print("M%d has a factor: %d" % (exponent, factor))
```