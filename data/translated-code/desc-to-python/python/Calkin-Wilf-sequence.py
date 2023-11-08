```python
def cw():
    # series generator code

def r2cf(num, den):
    # rational number to continued fraction code

def get_term_num(n, num, den):
    # calculate nth term of the series for given rational number

# demonstrate the use of functions
for i, term in enumerate(cw()):
    if i == 20:
        break
    print(term)

print(get_term_num(10, 3, 7))
```