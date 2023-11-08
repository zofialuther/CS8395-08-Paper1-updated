def makepowers():
    for i in range(1, 250):
        y = i * i * i * i * i
        pow5[i] = y

def within(a, bx, n):
    b = bx - 1
    for i in range(a, b):
        if i <= n:
            return True
    return False

def solution():
    makepowers()
    for x0 in range(4, 250):
        x0_5th = pow5[x0]
        for x1 in range(3, x0):
            x1_5th = pow5[x1]
            for x2 in range(2, x1):
                x2_5th = pow5[x2]
                for x3 in range(1, x2):
                    x3_5th = pow5[x3]
                    y_5th = x0_5th + x1_5th + x2_5th + x3_5th
                    for key, value in pow5.items():
                        if value == y_5th:
                            y = key
                            print(x0, x1, x2, x3, y)
                            return

solution()