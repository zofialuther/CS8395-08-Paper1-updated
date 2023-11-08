```python
def power(base, exponent, result):
    if exponent > 0:
        result = result * base
        exponent = exponent - 1
        return power(base, exponent, result)
    elif exponent < 0:
        result = result / base
        exponent = exponent + 1
        return power(base, exponent, result)
    else:
        return result

def exp_folder(base, exponent, Acc, Result):
    Result = Acc * base
    return Result
```