class semi_disk(path):
  def initialise(self, C, R, O, Col):
    CX = C.x
    CY = C.y
    choose(O, Deb, End)
    for I in range(Deb, End+1):
      X = R * cos(I * math.pi/180) + CX
      Y = R * sin(I * math.pi/180) + CY
      self.append(point(X, Y))
    self.closed(True)
    self.fill_pattern(Col)

def choose(O, Deb, End):
  if O == 's':
    Deb = 0
    End = 180
  elif O == 'n':
    Deb = 180
    End = 360
  elif O == 'w':
    Deb = 90
    End = 270
  elif O == 'e':
    Deb = -90
    End = 90

class disk(ellipse):
  def initialise(self, C, R, Col):
    self.super(R, R)
    self.center(C)
    self.pen(0)
    self.fill_pattern(Col)

def ying_yang(N):
  R = N * 100
  Title = 'Yin Yang ' + str(N)
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
  W.display(E, F, D1, D2, D3, D4)
  WD = 2 * R + 100
  W.size(size(WD, WD))
  W.open()