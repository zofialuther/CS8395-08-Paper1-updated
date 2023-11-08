```python
import javax.swing.JPanel
import java.awt.Color
import java.util.Timer
import java.util.TimerTask

class WolframCA(JPanel):
    ruleSet = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    cells = []
    rule = 90
    
    def __init__(self):
        self.setPreferredSize(800, 800)
        self.setBackground(Color.WHITE)
        self.cells = [[0]*self.getWidth() for _ in range(self.getHeight())]
        self.cells[self.getHeight()//2][self.getWidth()//2] = 1
        timer = Timer()
        timer.scheduleAtFixedRate(TimerTask(){
            self.rule = (self.rule + 1) % 256
            self.repaint()
        }, 0, 5000)
    
    def rules(self, a, b, c):
        if a == 1 and b == 1 and c == 1: return self.ruleSet[0]
        elif a == 1 and b == 1 and c == 0: return self.ruleSet[1]
        elif a == 1 and b == 0 and c == 1: return self.ruleSet[2]
        elif a == 1 and b == 0 and c == 0: return self.ruleSet[3]
        elif a == 0 and b == 1 and c == 1: return self.ruleSet[4]
        elif a == 0 and b == 1 and c == 0: return self.ruleSet[5]
        elif a == 0 and b == 0 and c == 1: return self.ruleSet[6]
        elif a == 0 and b == 0 and c == 0: return self.ruleSet[7]
    
    def drawCa(self, g):
        for i in range(1, self.getHeight()-1):
            for j in range(1, self.getWidth()-1):
                left = self.cells[i-1][j-1]
                center = self.cells[i-1][j]
                right = self.cells[i-1][j+1]
                self.cells[i][j] = self.rules(left, center, right)
                if self.cells[i][j] == 1:
                    g.fillRect(j, i, 1, 1)
    
    def drawLegend(self, g):
        g.drawString("Rule: " + str(self.rule), 10, 20)
    
    def paintComponent(self, g):
        self.drawCa(g)
        self.drawLegend(g)
    
if __name__ == "__main__":
    import javax.swing.JFrame
    frame = JFrame("Wolfram Cellular Automaton")
    ca = WolframCA()
    frame.add(ca)
    frame.setSize(800, 800)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setVisible(True)
```