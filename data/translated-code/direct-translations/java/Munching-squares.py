import javax.swing.JFrame
import javax.swing.JPanel
import java.awt.Color
import java.awt.Graphics

class XorPattern(JFrame):
    def __init__(self):
        xorPanel = JPanel()
        xorPanel.paint = self.paint_xor_panel
        self.add(xorPanel)
        self.setSize(300, 300)
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setVisible(True)
    
    def paint_xor_panel(self, g):
        for y in range(self.getHeight()):
            for x in range(self.getWidth()):
                g.setColor(Color(0, (x ^ y) % 256, 0))
                g.drawLine(x, y, x, y)

if __name__ == "__main__":
    XorPattern()