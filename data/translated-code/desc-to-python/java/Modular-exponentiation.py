```python
from math import pow

class PowMod:
    def main(self):
        a = 12345678901234567890
        b = 98765432109876543210
        m = 1000000007

        result = pow(a, b, m)
        print(result)

pow_mod = PowMod()
pow_mod.main()
```