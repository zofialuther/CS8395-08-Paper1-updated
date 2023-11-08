```python
from diagrams import Diagram, EqTriangle
from diagrams.backends import CairoCmdLine

triangle = EqTriangle().fill("black").stroke_width(0)

def reduce(t):
    return t | Diagram.VSpace(1) | (t + t)

sierpinski = [triangle]
for _ in range(7):
    sierpinski.append(reduce(sierpinski[-1]))

CairoCmdLine.main(sierpinski[-1])
```