```python
def cuboid():
  red = (1, 0, 0, 1)
  green = (0, 1, 0, 1)
  blue = (0, 0, 1, 1)
  front = [0,1,2,3]
  side = [4,1,5,3]
  top = [3,2,5,6]
  verts = [(0,0,1), (1,0,1), (0,1,1), (1,1,1), (1,0,0), (1,1,0), (0,1,0)]
  transform()
  render(front)
  render(side)
  render(top)

def render(vertices):
  for (x,y,z) in vertices:
    vertex(x, y, z)

def transform():
  translate(0, 0, -10)
  rotate(-14, 0, 0, 1)
  rotate(-30, 0, 1, 0)
  rotate(25, 1, 0, 0)
  scale(2, 3, 4)
  translate(-0.5, -0.5, -0.5)

def display():
  clear(ColorBuffer)
  perspective(40, 1, 1, 15)
  transform()
  cuboid()
  flush()

def main():
  name = "Cuboid"
  initialize(name, [])
  createWindow(name)
  displayCallback(display)
  mainLoop()
```