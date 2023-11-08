def fusc(i):
    if i < 1:
        return 0
    else:
        return first(go(i - 1))

def go(n):
    if n == 0:
        return (1, 0)
    elif n % 2 == 0:
        x, y = go(n // 2)
        return (x + y, y)
    else:
        x, y = go((n-1) // 2)
        return (x, x + y)

def main():
    print("First 61 terms:")
    for i in range(61):
        print(fusc(i))
    
    print("\n(Index, Value):")
    widths = generateWidths()
    for width in widths[:5]:
        print(width)

def generateWidths():
    result = []
    w = 2
    i = 0
    v = 0
    while len(str(v)) <= w:
        w, i, v = nextWidth(w, i, v)
        result.append((i, v))
    return result

def nextWidth(w, i, v):
    fi = (i, fusc(i))
    while len(str(v)) <= w:
        i += 1
        v = fusc(i)
    return (w + 1, i, v)