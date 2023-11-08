def play():
    initial = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    do_auto(50, initial)

def initial():
    return [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]

def do_auto(N, I):
    if N == 0:
        return
    for i in I:
        writ(i)
    print()
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

def apply1st(arr):
    A1 = r(arr[-2], arr[-1], arr[0])
    return A1

def apply(arr, prev, first, out):
    if len(arr) == 2:
        This = r(arr[0], arr[1], first)
        out.append(prev)
        out.append(This)
    else:
        This = r(arr[0], arr[1], arr[2])
        out.append(prev)
        out.append(This)
        apply(arr[1:], This, first, out)

def writ(num):
    if num == 0:
        print('.')
    else:
        print(1)