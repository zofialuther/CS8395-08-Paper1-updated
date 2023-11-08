import java.awt.Color
import java.awt.Graphics
import java.util
import javax.swing.JFrame

class DragonCurve(JFrame):
    
    def __init__(self, iter):
        super().__init__("Dragon Curve")
        self.setBounds(100, 100, 800, 600)
        self.setDefaultCloseOperation(EXIT_ON_CLOSE)
        self.turns = self.getSequence(iter)
        self.startingAngle = -iter * (Math.PI / 4)
        self.side = 400 / Math.pow(2, iter / 2.)
    
    def getSequence(self, iterations):
        turnSequence = []
        for i in range(iterations):
            copy = turnSequence.copy()
            copy.reverse()
            turnSequence.append(1)
            for turn in copy:
                turnSequence.append(-turn)
        return turnSequence
    
    def paint(self, g):
        g.setColor(Color.BLACK)
        angle = self.startingAngle
        x1, y1 = 230, 350
        x2 = x1 + int(Math.cos(angle) * self.side)
        y2 = y1 + int(Math.sin(angle) * self.side)
        g.drawLine(x1, y1, x2, y2)
        x1 = x2
        y1 = y2
        for turn in self.turns:
            angle += turn * (Math.PI / 2)
            x2 = x1 + int(Math.cos(angle) * self.side)
            y2 = y1 + int(Math.sin(angle) * self.side)
            g.drawLine(x1, y1, x2, y2)
            x1 = x2
            y1 = y2
    
    @staticmethod
    def main(args):
        DragonCurve(14).setVisible(True)