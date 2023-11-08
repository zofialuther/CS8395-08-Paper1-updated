```python
def ying_yang(N):
    R = N * 100
    Title = f'Yin Yang {N}'
    W = window(Title)
    Wh = colour(@default, 255*255, 255*255, 255*255)
    Bl = colour(@default, 0, 0, 0)
    CX = R + 50
    CY = R + 50
    R1 = R / 2
    R2 = R / 8
    CY1 = R1 + 50
    CY2 = 3 * R1 + 50

    E = semi_disk(point(CX, CY), R, 'w', Bl)
    F = semi_disk(point(CX, CY), R, 'e', Wh)
    D1 = disk(point(CX, CY1), R, Bl)
    D2 = disk(point(CX, CY2), R, Wh)
    D3 = disk(point(CX, CY1), R2, Wh)
    D4 = disk(point(CX, CY2), R2, Bl)

    W.display([E, F, D1, D2, D3, D4])
    WD = 2 * R + 100
    W.size(size(WD, WD))
    W.open()


class semi_disk(path):
    def initialise(self, C, R, O, Col):
        super().initialise()
        CX = C.x
        CY = C.y
        deb, end = choose(O)
        for i in range(deb, end):
            X = R * cos(i * pi/180) + CX
            Y = R * sin(i * pi/180) + CY
            self.append(point(X, Y))
        self.closed = @on
        self.fill_pattern = Col


def choose(O):
    if O == 's':
        return 0, 180
    elif O == 'n':
        return 180, 360
    elif O == 'w':
        return 90, 270
    elif O == 'e':
        return -90, 90


class disk(ellipse):
    def initialise(self, C, R, Col):
        super().initialise(R, R)
        self.center = C
        self.pen = 0
        self.fill_pattern = Col
```