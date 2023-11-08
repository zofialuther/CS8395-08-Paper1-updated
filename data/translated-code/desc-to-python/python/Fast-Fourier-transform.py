```python
import numpy as np

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    else:
        even = fft(x[::2])
        odd = fft(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([even + factor[:N//2] * odd, even + factor[N//2:] * odd])

input_array = np.array([0, 1, 2, 3])
fft_result = fft(input_array)
print(np.abs(fft_result))
```