```python
import math

def main():
    write_sierpinski_pentagon('sierpinski_pentagon.svg', 600, 5)

def write_sierpinski_pentagon(File, Size, Order):
    Stream = open(File, 'w')
    Stream.write(f"<svg xmlns='http://www.w3.org/2000/svg' width='{Size}' height='{Size}'>\n")
    Stream.write("<rect width='100%' height='100%' fill='white'/>\n")
    Margin = 5
    Radius = Size/2 - 2 * Margin
    Side = Radius * math.sin(math.pi/5) * 2
    Height = Side * (math.sin(math.pi/5) + math.sin(2 * math.pi/5))
    X = Size/2
    Y = (Size - Height)/2
    Scale_factor = 1/(2 + math.cos(2 * math.pi/5) * 2)
    sierpinski_pentagon(Stream, X, Y, Scale_factor, Side, Order)
    Stream.write("</svg>\n")
    Stream.close()

def sierpinski_pentagon(Stream, X, Y, _, Side, 1):
    Stream.write("<polygon stroke-width='1' stroke='black' fill='blue' points='")
    Stream.write(f"{X},{Y}")
    Angle = 6 * math.pi/5
    write_pentagon_points(Stream, Side, Angle, X, Y, 5)
    Stream.write("'/>\n")

def sierpinski_pentagon(Stream, X, Y, Scale_factor, Side, N):
    Side1 = Side * Scale_factor
    N1 = N - 1
    Angle = 6 * math.pi/5
    sierpinski_pentagons(Stream, X, Y, Scale_factor, Side1, Angle, N1, 5)

def write_pentagon_points(Stream, Side, Angle, X, Y, 0):
    return
def write_pentagon_points(Stream, Side, Angle, X, Y, N):
    N1 = N - 1
    X1 = X + math.cos(Angle) * Side
    Y1 = Y - math.sin(Angle) * Side
    Angle1 = Angle + 2 * math.pi/5
    Stream.write(f" {X1},{Y1}")
    write_pentagon_points(Stream, Side, Angle1, X1, Y1, N1)

def sierpinski_pentagons(Stream, X, Y, Scale_factor, Side, Angle, N, 0):
    return
def sierpinski_pentagons(Stream, X, Y, Scale_factor, Side, Angle, N, I):
    I1 = I - 1
    Distance = Side + Side * math.cos(2 * math.pi/5) * 2
    X1 = X + math.cos(Angle) * Distance
    Y1 = Y - math.sin(Angle) * Distance
    Angle1 = Angle + 2 * math.pi/5
    sierpinski_pentagon(Stream, X1, Y1, Scale_factor, Side, N)
    sierpinski_pentagons(Stream, X1, Y1, Scale_factor, Side, Angle1, N, I1)
```