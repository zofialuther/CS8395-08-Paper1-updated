```python
def cuboid(D1, D2, D3):
    W = D1 * 50
    H = D2 * 50
    D = D3 * 50

    C = window('cuboid')

    # compute the size of the window
    Width = W + math.ceil(math.sqrt(H * 48)) + 50
    Height = H + math.ceil(math.sqrt(H * 48)) + 50
    C.size = (Width, Height)

    # compute the top-left corner of the front face of the cuboid
    PX = 25
    PY = 25 + math.ceil(math.sqrt(H * 48))

    # colors of the faces
    C1 = (65535, 0, 0)
    C2 = (0, 65535, 0)
    C3 = (0, 0, 65535)

    # the front face
    B1 = box(W, H)
    B1.fill_pattern = C1
    C.display(B1, point(PX, PY))

    # the top face
    B2 = hpara(point(PX, PY), W, D, C2)
    C.display(B2)

    # the left face
    PX1 = PX + W
    B3 = vpara(point(PX1, PY), H, D, C3)
    C.display(B3)

    C.open()
```