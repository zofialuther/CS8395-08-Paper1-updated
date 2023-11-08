```python
def main():
    write_koch_snowflake('koch_snowflake.svg')

def write_koch_snowflake(File):
    with open(File, 'w') as Stream:
        koch_snowflake(Stream, 600, 5)

def koch_snowflake(Stream, Size, N):
    Stream.write(f"<svg xmlns='http://www.w3.org/2000/svg' width='{Size}' height='{Size}'>\n")
    Stream.write("<rect width='100%' height='100%' fill='black'/>\n")
    Stream.write("<path stroke-width='1' stroke='white' fill='none' d='")
    Sqrt3_2 = 0.86602540378444
    Length = Size * Sqrt3_2 * 0.95
    X0 = (Size - Length) / 2
    Y0 = Size / 2 - Length * Sqrt3_2 / 3
    X1 = X0 + Length / 2
    Y1 = Y0 + Length * Sqrt3_2
    X2 = X0 + Length
    Stream.write(f"M {X0},{Y0} ")
    koch_curve(Stream, X0, Y0, X1, Y1, N)
    koch_curve(Stream, X1, Y1, X2, Y0, N)
    koch_curve(Stream, X2, Y0, X0, Y0, N)
    Stream.write("z'/>\n</svg>\n")

def koch_curve(Stream, _, _, X1, Y1, N):
    if N == 0:
        Stream.write(f'L {X1},{Y1}\n')
    else:
        Sqrt3_2 = 0.86602540378444
        N1 = N - 1
        Dx = X1 - X0
        Dy = Y1 - Y0
        X2 = X0 + Dx / 3
        Y2 = Y0 + Dy / 3
        X3 = X0 + Dx / 2 - Dy * Sqrt3_2 / 3
        Y3 = Y0 + Dy / 2 + Dx * Sqrt3_2 / 3
        X4 = X0 + 2 * Dx / 3
        Y4 = Y0 + 2 * Dy / 3
        koch_curve(Stream, X0, Y0, X2, Y2, N1)
        koch_curve(Stream, X2, Y2, X3, Y3, N1)
        koch_curve(Stream, X3, Y3, X4, Y4, N1)
        koch_curve(Stream, X4, Y4, X1, Y1, N1)
```