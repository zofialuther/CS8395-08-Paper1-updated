```python
import java.awt.Color, java.awt.Graphics, javax.swing.JFrame

class FractalTree(JFrame):
    def __init__(self):
        self.setTitle("Fractal Tree")
        self.setBounds(100, 100, 800, 600)
        self.setResizable(False)
        self.setDefaultCloseOperation(EXIT_ON_CLOSE)

    def drawTree(self, g, x1, y1, angle, depth):
        if depth == 0:
            return
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        g.drawLine(x1, y1, x2, y2)
        self.drawTree(g, x2, y2, angle - 20, depth - 1)
        self.drawTree(g, x2, y2, angle + 20, depth - 1)

    def paint(self, g):
        g.setColor(Color.BLACK)
        self.drawTree(g, 400, 600, -90, 9)

    def main(self):
        fractal_tree = FractalTree()
        fractal_tree.setVisible(True)
```