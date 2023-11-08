```python
def polymul(p1, p2):
    return [p1[0]*p2[0], p1[0]*p2[1] + p1[1]*p2[0], p1[1]*p2[1]]

def mult_table(n):
    return map(lambda x: map(lambda y: (x,y), range(n)), range(n))

def digits(n):
    return map(int, str(n))

def digitSum(n):
    return reduce(lambda x, y: x*10 + y, n)

def longmult(num1, num2):
    return digitSum(reduce(lambda x, y: polymul(x,y), map(lambda x: map(lambda y: digits(num1)[x]*digits(num2)[y], range(len(digits(num2)))), range(len(digits(num1))))))
    
result = longmult(2**64, 2**64)
print(result)
```