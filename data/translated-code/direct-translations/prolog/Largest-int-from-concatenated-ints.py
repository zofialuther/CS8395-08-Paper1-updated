```python
def largest_int_v2(In, Out):
    LC = list(map(str, In))
    LCS = sorted(LC, key=my_sort)
    LC1 = LCS + LC
    Out = int(''.join(LC1))

def my_sort(L1, L2):
    V1 = L1 + L2
    I1 = int(''.join(V1))
    V2 = L2 + L1
    I2 = int(''.join(V2))
    if I1 < I2:
        return -1
    elif I1 == I2:
        return 0
    else:
        return 1

# particular case  95 958
def my_sort_special_1(L1, L2):
    H1 = L1[0]
    H2 = L2[0]
    if H1 > H2:
        return 1
    elif H1 < H2:
        return -1
    else:
        return 0

# particular case  958 95
def my_sort_special_2(L1, L2):
    H1 = L1[0]
    H2 = L2[0]
    if H1 > H2:
        return 1
    elif H1 < H2:
        return -1
    else:
        return 0
```