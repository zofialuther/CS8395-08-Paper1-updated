```python
def data(name, values):
    if name == "q":
        q = list(values)
    elif name == "q1":
        q1 = list(values)
    elif name == "q2":
        q2 = list(values)
    elif name == "r":
        r = values

def test():
    if "q" in locals():
        norm = abs(q)
        print(f'abs(q) is {norm}')
    if "q" in locals():
        nqx = -q
        print(f'negate(q) is {nqx}')
    if "q" in locals():
        nqx = q.conjugate()
        print(f'conjugate(q) is {nqx}')
    if "q1" in locals() and "q2" in locals():
        qx = [q1[i] + q2[i] for i in range(4)]
        print(f'q1+q2 is {qx}')
    if "q1" in locals() and "q2" in locals():
        qx = [q2[i] + q1[i] for i in range(4)]
        print(f'q2+q1 is {qx}')
    if "q" in locals() and "r" in locals():
        nqx = [q[i] * r for i in range(4)]
        print(f'q*r is {nqx}')
    if "q" in locals() and "r" in locals():
        nqx = [r * q[i] for i in range(4)]
        print(f'r*q is {nqx}')
    if "q1" in locals() and "q2" in locals():
        qx = [q1[i] * q2[i] for i in range(4)]
        print(f'q1*q2 is {qx}')
    if "q1" in locals() and "q2" in locals():
        qx = [q2[i] * q1[i] for i in range(4)]
        print(f'q2*q1 is {qx}')
```