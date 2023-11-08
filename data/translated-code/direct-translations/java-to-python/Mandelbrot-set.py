import java.awt.Graphics
import java.awt.image.BufferedImage
import javax.swing.JFrame

class Mandelbrot(JFrame):

    MAX_ITER = 570
    ZOOM = 150
    I = None
    zx = 0
    zy = 0
    cX = 0
    cY = 0
    tmp = 0

    def __init__(self):
        super().__init__("Mandelbrot Set")
        self.setBounds(100, 100, 800, 600)
        self.setResizable(False)
        self.setDefaultCloseOperation(EXIT_ON_CLOSE)
        self.I = BufferedImage(self.getWidth(), self.getHeight(), BufferedImage.TYPE_INT_RGB)
        for y in range(self.getHeight()):
            for x in range(self.getWidth()):
                self.zx = self.zy = 0
                self.cX = (x - 400) / self.ZOOM
                self.cY = (y - 300) / self.ZOOM
                iter = self.MAX_ITER
                while self.zx * self.zx + self.zy * self.zy < 4 and iter > 0:
                    self.tmp = self.zx * self.zx - self.zy * self.zy + self.cX
                    self.zy = 2.0 * self.zx * self.zy + self.cY
                    self.zx = self.tmp
                    iter -= 1
                self.I.setRGB(x, y, iter | (iter << 8))

    def paint(self, g):
        g.drawImage(self.I, 0, 0, self)

    @staticmethod
    def main(args):
        Mandelbrot().setVisible(True)