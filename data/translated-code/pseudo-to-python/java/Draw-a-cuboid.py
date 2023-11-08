import java.awt.*
import java.awt.event.*
import static java.lang.Math.*
import javax.swing.*

class Cuboid(JPanel):
    nodes = [[-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1],
             [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]]
    edges = [[0, 1], [1, 3], [3, 2], [2, 0], [4, 5], [5, 7], [7, 6],
             [6, 4], [0, 4], [1, 5], [2, 6], [3, 7]]
    mouseX = 0
    prevMouseX = 0
    mouseY = 0
    prevMouseY = 0

    def __init__(self):
        self.setPreferredSize(Dimension(640, 640))
        self.setBackground(Color.white)
        
        self.scale(80, 120, 160)
        self.rotateCube(PI / 5, PI / 9)
        
        self.addMouseListener(MouseAdapter(
            mousePressed=self.mousePressed,
            mouseDragged=self.mouseDragged
        ))

    def scale(self, sx, sy, sz):
        for node in self.nodes:
            node[0] *= sx
            node[1] *= sy
            node[2] *= sz

    def rotateCube(self, angleX, angleY):
        sinX = sin(angleX)
        cosX = cos(angleX)

        sinY = sin(angleY)
        cosY = cos(angleY)

        for node in self.nodes:
            x = node[0]
            y = node[1]
            z = node[2]

            node[0] = x * cosX - z * sinX
            node[2] = z * cosX + x * sinX

            z = node[2]

            node[1] = y * cosY - z * sinY
            node[2] = z * cosY + y * sinY

    def drawCube(self, g):
        g.translate(self.getWidth() / 2, self.getHeight() / 2)

        for edge in self.edges:
            xy1 = self.nodes[edge[0]]
            xy2 = self.nodes[edge[1]]
            g.drawLine(round(xy1[0]), round(xy1[1]), round(xy2[0]), round(xy2[1]))

        for node in self.nodes:
            g.fillOval(round(node[0]) - 4, round(node[1]) - 4, 8, 8)

    def paintComponent(self, gg):
        super().paintComponent(gg)
        g = gg
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON)

        self.drawCube(g)

def main(args):
    SwingUtilities.invokeLater(lambda: 
        f = JFrame()
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        f.setTitle("Cuboid")
        f.setResizable(False)
        f.add(Cuboid(), BorderLayout.CENTER)
        f.pack()
        f.setLocationRelativeTo(None)
        f.setVisible(True)
    )