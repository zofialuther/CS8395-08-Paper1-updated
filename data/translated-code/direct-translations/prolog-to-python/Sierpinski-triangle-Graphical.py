def sierpinski(N):
    A = 'Sierpinski order {}'.format(N)
    D = picture(A)
    draw_Sierpinski(D, N, point(350, 50), 600)
    D.size = (690, 690)
    D.open()

def draw_Sierpinski(Window, 1, point(X, Y), Len):
    X1 = X - round(Len/2)
    X2 = X + round(Len/2)
    Y1 = Y + Len * sqrt(3) / 2
    Pa = path()
    Pa.append(point(X, Y))
    Pa.append(point(X1, Y1))
    Pa.append(point(X2, Y1))
    Pa.closed = True
    Pa.fill_pattern = colour(@default, 0, 0, 0)

def draw_Sierpinski(Window, N, point(X, Y), Len):
    Len1 = round(Len/2)
    X1 = X - round(Len/4)
    X2 = X + round(Len/4)
    Y1 = Y + Len * sqrt(3) / 4
    N1 = N - 1
    draw_Sierpinski(Window, N1, point(X, Y), Len1)
    draw_Sierpinski(Window, N1, point(X1, Y1), Len1)
    draw_Sierpinski(Window, N1, point(X2, Y1), Len1)