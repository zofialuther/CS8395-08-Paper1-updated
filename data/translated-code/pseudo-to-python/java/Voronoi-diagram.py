from java.awt import Color, Graphics, Graphics2D, geom
from java.awt.image import BufferedImage
from java.io import File, IOException
from java.util import Random
from javax.imageio import ImageIO
from javax.swing import JFrame

class Voronoi(JFrame):
    p = 3
    I = BufferedImage
    px = []
    py = []
    color = []
    cells = 100
    size = 1000
    
    def __init__(self):
        self.title = "Voronoi"
        self.setSize(self.size, self.size)
        n = 0
        rand = Random()
        self.I = BufferedImage(self.size, self.size, BufferedImage.TYPE_INT_RGB)
        self.px = [0]*self.cells
        self.py = [0]*self.cells
        self.color = [0]*self.cells
        
        for i in range(self.cells):
            self.px[i] = rand.nextInt(self.size)
            self.py[i] = rand.nextInt(self.size)
            self.color[i] = Color(rand.nextInt(255), rand.nextInt(255), rand.nextInt(255))
        
        for x in range(self.size):
            for y in range(self.size):
                min_dist = distance(self.size, self.size)
                index = -1
                for i in range(self.cells):
                    d = distance(x - self.px[i], y - self.py[i])
                    if d < min_dist:
                        min_dist = d
                        index = i
                self.I.setRGB(x, y, self.color[index].getRGB())
        
        g = self.I.createGraphics()
        g.setColor(Color.BLACK)
        for i in range(self.cells):
            g.fill(geom.Ellipse2D.Double(self.px[i], self.py[i], 3, 3))
        
        try:
            ImageIO.write(self.I, "png", File("voronoi.png"))
        except IOException as e:
            e.printStackTrace()
    
    def paint(self, g):
        g.drawImage(self.I, 0, 0, self)
    
    @staticmethod
    def distance(x, y):
        return Math.sqrt(x * x + y * y)
    
    @staticmethod
    def main(args):
        voronoi = Voronoi()
        voronoi.setVisible(True)