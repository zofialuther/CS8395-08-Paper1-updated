```python
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;

class XorPattern(JFrame):
    private JPanel xorPanel;

    def __init__(self):
        xorPanel = JPanel():
            def paint(self, g: Graphics):
                for x in range(self.getWidth()):
                    for y in range(self.getHeight()):
                        g.setColor(Color(x ^ y % 256, x ^ y % 256, x ^ y % 256))
                        g.drawLine(x, y, x, y)

        self.add(xorPanel)
        self.setSize(300, 300)
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setVisible(True)

def main():
    xorPattern = XorPattern()

if __name__ == "__main__":
    main()
```