```python
def custom_power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * custom_power(base, exponent - 1)
    else:
        raise ValueError("Exponent must be a non-negative integer")
```