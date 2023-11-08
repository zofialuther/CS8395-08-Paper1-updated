```python
def play():
    I = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    do_auto(50, I)

def initial():
    return [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]

def do_auto(N, I):
    if N == 0:
        return
    print(''.join(map(str, I)))
    Next = apply_rules(I)
    N1 = N - 1
    do_auto(N1, Next)

def r(a, b, c, d):
    rules = {
        (0,0,0): 0,
        (0,0,1): 1,
        (0,1,0): 0,
        (0,1,1): 1,
        (1,0,0): 1,
        (1,0,1): 0,
        (1,1,0): 1,
        (1,1,1): 0
    }
    return rules[(a, b, c)]

def apply_rules(In):
    First = apply1st(In)
    Out = [First]
    apply(In, First, First, Out)
    return Out

def apply1st(T):
    A1 = r(T[-2], T[-1], T[0])
    return A1

def apply(T, Prev, First, Out):
    if len(T) == 2:
        This = r(T[0], T[1], First)
        Out.append(This)
    else:
        This = r(T[0], T[1], T[2])
        Out.append(This)
        apply(T[1:], This, First, Out)

def writ(num):
    if num == 0:
        print('.')
    elif num == 1:
        print(1)

play()
```