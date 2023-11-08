import java.awt.Color
import java.awt.Dimension
import java.awt.Graphics
import javax.swing.JFrame
import javax.swing.JPanel
import javax.swing.SwingUtilities
import javax.swing.WindowConstants

class BresenhamPanel(JPanel):
    def __init__(self):
        self.pixelSize = 10
        self.setPreferredSize(Dimension(600, 500))
        self.setBackground(Color.WHITE)

    def paintComponent(self, g):
        super().paintComponent(g)
        w = (self.getWidth() - 1) // self.pixelSize
        h = (self.getHeight() - 1) // self.pixelSize
        maxX = (w - 1) // 2
        maxY = (h - 1) // 2
        x1, x2, x3, x4 = -maxX, maxX * -2 // 3, maxX * 2 // 3, maxX
        y1, y2, y3, y4 = -maxY, maxY * -2 // 3, maxY * 2 // 3, maxY
        self.drawLine(g, 0, 0, x3, y1)  # NNE
        self.drawLine(g, 0, 0, x4, y2)  # ENE
        self.drawLine(g, 0, 0, x4, y3)  # ESE
        self.drawLine(g, 0, 0, x3, y4)  # SSE
        self.drawLine(g, 0, 0, x2, y4)  # SSW
        self.drawLine(g, 0, 0, x1, y3)  # WSW
        self.drawLine(g, 0, 0, x1, y2)  # WNW
        self.drawLine(g, 0, 0, x2, y1)  # NNW

    def plot(self, g, x, y):
        w = (self.getWidth() - 1) // self.pixelSize
        h = (self.getHeight() - 1) // self.pixelSize
        maxX = (w - 1) // 2
        maxY = (h - 1) // 2
        borderX = self.getWidth() - ((2 * maxX + 1) * self.pixelSize + 1)
        borderY = self.getHeight() - ((2 * maxY + 1) * self.pixelSize + 1)
        left = (x + maxX) * self.pixelSize + borderX // 2
        top = (y + maxY) * self.pixelSize + borderY // 2
        g.setColor(Color.BLACK)
        g.drawOval(left, top, self.pixelSize, self.pixelSize)

    def drawLine(self, g, x1, y1, x2, y2):
        d = 0
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        dx2 = 2 * dx
        dy2 = 2 * dy
        ix = 1 if x1 < x2 else -1
        iy = 1 if y1 < y2 else -1
        x = x1
        y = y1
        if dx >= dy:
            while True:
                self.plot(g, x, y)
                if x == x2:
                    break
                x += ix
                d += dy2
                if d > dx:
                    y += iy
                    d -= dx2
        else:
            while True:
                self.plot(g, x, y)
                if y == y2:
                    break
                y += iy
                d += dx2
                if d > dy:
                    x += ix
                    d -= dy2

def run():
    f = JFrame()
    f.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)
    f.setTitle("Bresenham")
    f.getContentPane().add(BresenhamPanel())
    f.pack()
    f.setLocationRelativeTo(None)
    f.setVisible(True)

def main():
    SwingUtilities.invokeLater(run)

if __name__ == "__main__":
    main()