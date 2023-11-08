```python
import sys
import java.awt.Color as Color
import java.awt.Dimension as Dimension
import java.awt.Graphics as Graphics
import java.awt.Graphics2D as Graphics2D
import javax.swing.JFrame as JFrame
import javax.swing.JPanel as JPanel

def main():
    i = 3
    if len(sys.argv) >= 2:
        try:
            i = int(sys.argv[1])
        except ValueError as e:
            print("Usage: 'java SierpinskyTriangle [level]'\nNow setting level to " + str(i))
    level = i

    frame = JFrame("Sierpinsky Triangle - Java")
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)

    panel = JPanel()
    def paintComponent(g):
        g.setColor(Color.BLACK)
        drawSierpinskyTriangle(level, 20, 20, 360, g)
    panel.setPreferredSize(Dimension(400, 400))

    frame.add(panel)
    frame.pack()
    frame.setResizable(False)
    frame.setLocationRelativeTo(None)
    frame.setVisible(True)

def drawSierpinskyTriangle(level, x, y, size, g):
    if level <= 0:
        return

    g.drawLine(x, y, x+size, y)
    g.drawLine(x, y, x, y+size)
    g.drawLine(x+size, y, x, y+size)

    drawSierpinskyTriangle(level-1, x, y, size/2, g)
    drawSierpinskyTriangle(level-1, x+size/2, y, size/2, g)
    drawSierpinskyTriangle(level-1, x, y+size/2, size/2, g)
```