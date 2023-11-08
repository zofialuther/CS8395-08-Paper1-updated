from bitmap import *
from bitmapIO import *
from clpfd import *

def draw_recursive_line(NPict, Pict, Color, X, X, _DX, _DY, Y, Y, _E, _Sx, _Sy):
    set_pixel0(NPict, Pict, [X, Y], Color)

def draw_recursive_line(NPict, Pict, Color, X, X2, DX, DY, Y, Y2, E, Sx, Sy):
    set_pixel0(TPict, Pict, [X, Y], Color)
    E2 = 2 * E

    if E2 >= DY:
        Ey = 1
        NX = X + Sx
    else:
        Ey = 0
        NX = X

    if E2 <= DX:
        Ex = 1
        NY = Y + Sy
    else:
        Ex = 0
        NY = Y

    NE = E + DX * Ex + DY * Ey
    draw_recursive_line(NPict, TPict, Color, NX, X2, DX, DY, NY, Y2, NE, Sx, Sy)

def draw_line(NPict, Pict, Color, X1, Y1, X2, Y2):
    DeltaY = Y2 - Y1
    DeltaX = X2 - X1

    if DeltaY < 0:
        Sy = -1
    else:
        Sy = 1

    if DeltaX < 0:
        Sx = -1
    else:
        Sx = 1

    DX = abs(DeltaX)
    DY = -1 * abs(DeltaY)
    E = DY + DX
    draw_recursive_line(NPict, Pict, Color, X1, X2, DX, DY, Y1, Y2, E, Sx, Sy)

def init():
    B = new_bitmap([100, 100], [255, 255, 255])
    NB = draw_line(B, [0, 0, 0], 2, 2, 10, 90)
    write_ppm_p6('line.ppm', NB)