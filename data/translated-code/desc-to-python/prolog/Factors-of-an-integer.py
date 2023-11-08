```python
def factor(a, b):
    return a % b == 0

def smart_factors(N, Fs):
    if N > 0:
        setof(Fs, factor(N, Fs), Fs)
```