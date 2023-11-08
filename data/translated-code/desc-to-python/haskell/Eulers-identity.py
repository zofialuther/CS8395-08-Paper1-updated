```python
import Data.Complex

def eulerIdentityZeroIsh():
    small_deviation = 0.00001
    result = Data.Complex.exp(Data.Complex.i * small_deviation)
    return result

def main():
    print(eulerIdentityZeroIsh())

main()
```