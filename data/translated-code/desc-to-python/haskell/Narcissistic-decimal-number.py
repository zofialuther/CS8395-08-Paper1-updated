```python
def powerSum(num, power):
    return sum(int(digit)**power for digit in str(num))

def isDaffodil(num, power):
    return num == powerSum(num, power)

def digitList(num):
    return [int(digit) for digit in str(num)]

def narcissiOfLength(nDigits):
    results = []
    for num in range(10**(nDigits-1), 10**nDigits):
        if isDaffodil(num, nDigits):
            results.append(num)
    return results

def main():
    for i in range(1, 8):
        numbers = narcissiOfLength(i)
        print(f"Numbers of length {i}: {numbers}")

def fTable(data):
    # Function to display data in a formatted table
    pass
```