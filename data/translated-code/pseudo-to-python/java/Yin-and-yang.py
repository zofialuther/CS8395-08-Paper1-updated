```python
import java.awt.Color
import java.awt.Graphics
import java.awt.Image
import java.awt.image.BufferedImage
import javax.swing.ImageIcon
import javax.swing.JFrame
import javax.swing.JLabel

class YinYangGenerator:
    def __init__(self, size):
        self.size = size

    def drawYinYang(self, graphics):
        colorSave = graphics.getColor()
        graphics.setColor(Color.WHITE)
        graphics.fillOval(0, 0, self.size-1, self.size-1)
        graphics.setColor(Color.BLACK)
        graphics.fillArc(0, 0, self.size-1, self.size-1, 270, 180)
        graphics.fillOval(self.size//4, self.size//2, self.size//2, self.size//2)
        graphics.setColor(Color.WHITE)
        graphics.fillOval(self.size//4, 0, self.size//2, self.size//2)
        graphics.fillOval(7*self.size//16, 11*self.size//16, self.size//8, self.size//8)
        graphics.setColor(Color.BLACK)
        graphics.fillOval(7*self.size//16, 3*self.size//16, self.size//8, self.size//8)
        graphics.drawOval(0, 0, self.size-1, self.size-1)
        graphics.setColor(colorSave)

    def createImage(self, bg):
        image = BufferedImage(self.size, self.size, BufferedImage.TYPE_INT_RGB)
        graphics = image.getGraphics()
        graphics.setColor(bg)
        graphics.fillRect(0,0,self.size,self.size)
        self.drawYinYang(graphics)
        return image

    def main(self, args):
        size = Integer.parseInt(args[0])
        generator = YinYangGenerator(size)
        frame = JFrame("Yin Yang Generator")
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        yinYang = generator.createImage(frame.getBackground())
        frame.add(JLabel(ImageIcon(yinYang)))
        frame.pack()
        frame.setVisible(True)
```