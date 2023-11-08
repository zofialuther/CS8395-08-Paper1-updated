```python
def uncurry(func):
    def wrapper(*args):
        return func(*args)
    return wrapper

def half_adder(a, b):
    sum = a ^ b
    carry = a & b
    return (sum, carry)

@uncurry
def full_adder(carry, a, b):
    sum1, carry1 = half_adder(a, b)
    sum2, carry2 = half_adder(sum1, carry)
    final_sum = sum2
    final_carry = carry1 or carry2
    return (final_sum, final_carry)

def adder4(inputs):
    results = []
    carry = 0
    for input_set in inputs:
        result, carry = full_adder(carry, input_set[0], input_set[1])
        results.append(result)
    return results
```