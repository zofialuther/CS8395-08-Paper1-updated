```python
# initial condition
def do(V):
    if V == 0:
        print(0)
        do(1)

# control condition
def do(V):
    if V % 6 == 0:
        return False

# loop
def do(V):
    print(V)
    Y = V + 1
    do(Y)

def wloop():
    do(0)
```