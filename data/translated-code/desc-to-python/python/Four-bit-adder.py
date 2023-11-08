```python
def xor_gate(a, b):
    return a ^ b

def half_adder(a, b):
    sum = xor_gate(a, b)
    carry = a & b
    return sum, carry

def full_adder(a, b, c):
    sum1, carry1 = half_adder(a, b)
    sum2, carry2 = half_adder(sum1, c)
    carry = carry1 | carry2
    return sum2, carry

def int_to_binary_bus(num):
    return [int(x) for x in bin(num)[2:].zfill(4)]

def test_full_adder():
    for i in range(16):
        for j in range(16):
            a = int_to_binary_bus(i)
            b = int_to_binary_bus(j)
            carry = 0
            result = []
            for k in range(4):
                sum, carry = full_adder(a[k], b[k], carry)
                result.insert(0, sum)
            print(f"{a} + {b} = {result}, Carry: {carry}")

if __name__ == "__main__":
    test_full_adder()
```