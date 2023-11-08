```python
def sierpinski(N):
    A = 'Sierpinski order ' + str(N)
    D = Picture(A)
    drawSierpinski(D, N, Point(350, 50), 600)
    D.setSize(Size(690, 690))
    D.open()

def drawSierpinski(Window, N, Point(X, Y), Len):
    if N == 1:
        X1 = X - round(Len / 2)
        X2 = X + round(Len / 2)
        Y1 = Y + Len * math.sqrt(3) / 2
        Pa = Path()
        Pa.append(Point(X, Y))
        Pa.append(Point(X1, Y1))
        Pa.append(Point(X2, Y1))
        Pa.closed = True
        Pa.fillPattern = Colour(0, 0, 0)
        Window.display(Pa)
    else:
        Len1 = round(Len / 2)
        X1 = X - round(Len / 4)
        X2 = X + round(Len / 4)
        Y1 = Y + Len * math.sqrt(3) / 4
        N1 = N - 1
        drawSierpinski(Window, N1, Point(X, Y), Len1)
        drawSierpinski(Window, N1, Point(X1, Y1), Len1)
        drawSierpinski(Window, N1, Point(X2, Y1), Len1)
```