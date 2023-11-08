```python
import random

def dutch_flag(N):
    L = [init() for _ in range(N)]
    while not is_dutch_flag(L):
        print(L)
        test_sorted(L)
        TmpFlag = sort_dutch_flag(L)
        Flag = [item for sublist in TmpFlag for item in sublist]
        print(Flag)
        test_sorted(Flag)

def init():
    return random.choice(['blue', 'red', 'white'])

def sort_dutch_flag(L):
    R, W, B = [], [], []
    for color in L:
        if color == 'red':
            R.append(color)
        elif color == 'white':
            W.append(color)
        else:
            B.append(color)
    return [R, W, B]

def is_dutch_flag(Flag):
    return Flag[0] == 'red' and Flag[-1] == 'blue' and Flag.count('red') + Flag.count('white') + Flag.count('blue') == len(Flag)

def test_sorted(Flag):
    if is_dutch_flag(Flag):
        print('it is a dutch flag')
    else:
        print('it is not a dutch flag')
    print()

dutch_flag(10)
```