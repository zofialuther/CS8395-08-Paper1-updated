```python
def polymul(p1, p2):
    return [sum(p1[i]*p2[j] for i in range(len(p1)) if i+j == k) for k in range(len(p1)+len(p2)-1)]

def digits(n):
    return [int(x) for x in str(n)]

def longmult(x, y):
    return int(''.join(map(str, polymul(digits(x), digits(y))))

if __name__ == "__main__":
    result = longmult(2**64, 2**64)
    print(result)
```