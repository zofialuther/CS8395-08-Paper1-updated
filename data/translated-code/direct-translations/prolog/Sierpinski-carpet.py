def main():
    write_sierpinski_carpet('sierpinski_carpet.svg', 486, 4)

def write_sierpinski_carpet(File, Size, Order):
    with open(File, 'w') as Stream:
        Stream.write(f"<svg xmlns='http://www.w3.org/2000/svg' width='{Size}' height='{Size}'>\n")
        Stream.write("<rect width='100%' height='100%' fill='white'/>\n")
        Side = Size / 3.0
        sierpinski_carpet(Stream, 0, 0, Side, Order)
        Stream.write("</svg>\n")

def sierpinski_carpet(Stream, X, Y, Side, Order):
    if Order == 0:
        X0 = X + Side
        Y0 = Y + Side
        write_square(Stream, X0, Y0, Side)
    else:
        Order1 = Order - 1
        Side1 = Side / 3.0
        X0 = X + Side
        Y0 = Y + Side
        X1 = X0 + Side
        Y1 = Y0 + Side
        write_square(Stream, X0, Y0, Side)
        sierpinski_carpet(Stream, X, Y, Side1, Order1)
        sierpinski_carpet(Stream, X0, Y, Side1, Order1)
        sierpinski_carpet(Stream, X1, Y, Side1, Order1)
        sierpinski_carpet(Stream, X, Y0, Side1, Order1)
        sierpinski_carpet(Stream, X1, Y0, Side1, Order1)
        sierpinski_carpet(Stream, X, Y1, Side1, Order1)
        sierpinski_carpet(Stream, X0, Y1, Side1, Order1)
        sierpinski_carpet(Stream, X1, Y1, Side1, Order1)

def write_square(Stream, X, Y, Side):
    Stream.write(f"<rect fill='black' x='{X}' y='{Y}' width='{Side}' height='{Side}'/>\n")

main()