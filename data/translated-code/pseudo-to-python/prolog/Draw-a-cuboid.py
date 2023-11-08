def cuboid(D1, D2, D3):
    W = D1 * 50
    H = D2 * 50
    D = D3 * 50
    C = window.cuboid()
    Width = W + math.ceil(math.sqrt(H * 48)) + 50
    Height = H + math.ceil(math.sqrt(H * 48)) + 50
    C.size = size(Width, Height)
    PX = 25
    PY = 25 + math.ceil(math.sqrt(H * 48))
    C1 = colour(65535, 0, 0)
    C2 = colour(0, 65535, 0)
    C3 = colour(0, 0, 65535)
    B1 = box(W, H)
    B1.fill_pattern = C1
    C.display(B1, point(PX, PY))
    B2 = hpara(point(PX, PY), W, D, C2)
    C.display(B2)
    PX1 = PX + W
    B3 = vpara(point(PX1, PY), H, D, C3)
    C.display(B3)
    C.open()
  
def hpara(path, P, Pos, Width, Height, Color):
    P.initialise()
    P.append(Pos)
    H = math.ceil(math.sqrt(Height * 48))
    X = Pos.x
    Y = Pos.y
    X1 = X + H
    Y1 = Y - H
    P.append(point(X1, Y1))
    X2 = X1 + Width
    P.append(point(X2, Y1))
    X3 = X2 - H
    P.append(point(X3, Pos.y))
    P.append(Pos)
    P.fill_pattern = Color

def vpara(path, P, Pos, Height, Depth, Color):
    P.initialise()
    P.append(Pos)
    H = math.ceil(math.sqrt(Depth * 48))
    X = Pos.x
    Y = Pos.y
    X1 = X + H
    Y1 = Y - H
    P.append(point(X1, Y1))
    Y2 = Y1 + Height
    P.append(point(X1, Y2))
    Y3 = Y2 + H
    P.append(point(X, Y3))
    P.append(Pos)
    P.fill_pattern = Color