```python
def main():
    write_sierpinski_pentagon('sierpinski_pentagon.svg', 600, 5)

def write_sierpinski_pentagon(File, Size, Order):
    with open(File, 'w') as Stream:
        Stream.write(f"<svg xmlns='http://www.w3.org/2000/svg' width='{Size}' height='{Size}'>\n")
        Stream.write("<rect width='100%' height='100%' fill='white'/>\n")
        Margin = 5
        Radius = Size/2 - 2 * Margin
        Side = Radius * sin(pi/5) * 2
        Height = Side * (sin(pi/5) + sin(2 * pi/5))
        X = Size/2
        Y = (Size - Height)/2
        Scale_factor = 1/(2 + cos(2 * pi/5) * 2)
        sierpinski_pentagon(Stream, X, Y, Scale_factor, Side, Order)
        Stream.write("</svg>\n")

def sierpinski_pentagon(Stream, X, Y, _, Side, 1):
    Stream.write("<polygon stroke-width='1' stroke='black' fill='blue' points='")
    Stream.write(f'{X},{Y}')
    Angle = 6 * pi/5
    write_pentagon_points(Stream, Side, Angle, X, Y, 5)
    Stream.write("'/>\n")
    
def sierpinski_pentagon(Stream, X, Y, Scale_factor, Side, N):
    Side1 = Side * Scale_factor
    N1 = N - 1
    Angle = 6 * pi/5
    sierpinski_pentagons(Stream, X, Y, Scale_factor, Side1, Angle, N1, 5)

def write_pentagon_points(Stream, Side, Angle, X, Y, N):
    if N == 0:
        return
    else:
        N1 = N - 1
        X1 = X + cos(Angle) * Side
        Y1 = Y - sin(Angle) * Side
        Angle1 = Angle + 2 * pi/5
        Stream.write(f' {X1},{Y1}')
        write_pentagon_points(Stream, Side, Angle1, X1, Y1, N1)

def sierpinski_pentagons(Stream, X, Y, Scale_factor, Side, Angle, N, I):
    if I == 0:
        return
    else:
        I1 = I - 1
        Distance = Side + Side * cos(2 * pi/5) * 2
        X1 = X + cos(Angle) * Distance
        Y1 = Y - sin(Angle) * Distance
        Angle1 = Angle + 2 * pi/5
        sierpinski_pentagon(Stream, X1, Y1, Scale_factor, Side, N)
        sierpinski_pentagons(Stream, X1, Y1, Scale_factor, Side, Angle1, N, I1)

main()
```