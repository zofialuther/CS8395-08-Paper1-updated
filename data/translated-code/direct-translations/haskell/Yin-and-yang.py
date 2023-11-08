```python
from diagrams import Diagram, Circle, Square

perim = Arc(0, 360).scale(1/2)
torus_c = Circle(1).fill("white") + Circle(1/3).fill("black")
torus_c_prime = Circle(1).fill("black") + Circle(1/3).fill("white")
xform = Transform().translateY(1/4).scale(1/4)
base = Square(1, 1).fill("white") + Square(1, 1).fill("black")

yinyang = Diagram().line_width(0).append(perim.line_width(0.003), torus_c.xform(xform), torus_c_prime.xform(xform.negate()), base.clip_by(perim))

main = Diagram().default_main().padding(1.1).beside(yinyang, yinyang.scale(1/4), direction=(2, -1))
```