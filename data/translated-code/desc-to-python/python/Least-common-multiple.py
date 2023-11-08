```python
import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def gcd(a, b):
    return math.gcd(a, b)

def test_lcm_gcd():
    assert lcm(12, 15) == 60
    assert gcd(12, 15) == 3
    assert lcm(5, 7) == 35
    assert gcd(5, 7) == 1

def main():
    test_lcm_gcd()
    print("All test cases passed!")

if __name__ == "__main__":
    main()
```