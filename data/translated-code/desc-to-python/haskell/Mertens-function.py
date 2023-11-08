```python
from sympy import primefactors
from sympy.ntheory import mobius
from sympy import mertens
import numpy as np

def mobius_function(n):
    return mobius(n)

def mertens_function(n):
    return mertens(n)

def analyze_mertens_function():
    mertens_values = [mertens_function(i) for i in range(1, 100)]
    num_zeros = np.count_nonzero(np.array(mertens_values) == 0)
    num_cross_zero = np.count_nonzero(np.diff(np.sign(mertens_values)))
    print("Number of zeros in Mertens function for range 1 to 99:", num_zeros)
    print("Number of times Mertens function crosses zero for range 1 to 99:", num_cross_zero)

analyze_mertens_function()
```