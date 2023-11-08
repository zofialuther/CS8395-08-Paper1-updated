```python
import math

def gammaln(x):
    cof = [76.18009172947146, -86.50532032941677, 24.01409824083091, -1.231739572450155, 0.1208650973866179e-2, -0.5395239384953e-5]
    ser = 1.000000000190015
    y = x
    tmp = x + 5.5
    tmp -= (x + 0.5) * math.log(tmp)
    ser = 1.000000000190015
    for j in range(6):
        y += 1
        ser += cof[j] / y
    return -tmp + math.log(2.5066282746310005 * ser / x)

def main():
    values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    for value in values:
        result = gammaln(value)
        print(f"The natural logarithm of the gamma function for {value} is {result}")

main()
```