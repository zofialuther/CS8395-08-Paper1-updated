```python
import random
import turtle

def maze(Lig,Col):
    for l in range(Lig+1):
        XL = 50
        YL = l * 30 + 50
        XR = Col * 30 + 50
        createLine(XL, YL, XR, YL)
    
    for c in range(Col+1):
        XT = 50 + c * 30
        YT = 50
        YB = Lig * 30 + 50
        createLine(XT, YT, XT, YB)
    
    SX = Col * 30 + 100
    SY = Lig * 30 + 100
    turtle.setworldcoordinates(0, SY, SX, 0)
    
    L0 = random.randint(0, Lig-1)
    C0 = random.randint(0, Col-1)
    assertCell(L0, C0)
    search(Lig, Col, L0, C0)

def search(Lig, Col, L, C):
    Dir = random.randint(0, 3)
    L1, C1 = nextcell(Dir, Lig, Col, L, C)
    assertCell(L1, C1)
    erase_line(L, C, L1, C1)
    search(Lig, Col, L1, C1)

def erase_line(L, C, L1, C1):
    if C < C1:
        C2 = C1
    else:
        C2 = C
    XT = C2 * 30 + 50
    YT = L * 30 + 51
    YR = (L + 1) * 30 + 50
    createLine(XT, YT, XT, YR, 'white')

def nextcell(Dir, Lig, Col, L, C):
    if next(Dir, Lig, Col, L, C, L1, C1):
        return (L1, C1)
    elif next(Dir1, Lig, Col, L, C, L1, C1):
        return (L1, C1)
    elif next(Dir2, Lig, Col, L, C, L1, C1):
        return (L1, C1)
    elif next(Dir3, Lig, Col, L, C, L1, C1):
        return (L1, C1)

def next(direction, Lig, Col, L, C):
    if direction == 0:
        if L > 0 and not cell(L1, C):
            return True
    # similar for other directions
```