import java.awt
import java.awt.event.ActionEvent
import javax.swing
import javax.swing.Timer

class WolframCA(JPanel):
    ruleSet = [30, 45, 50, 57, 62, 70, 73, 75, 86, 89, 90, 99, 101, 105, 109, 110, 124, 129, 133, 135, 137, 139, 141, 164, 170, 232]
    cells = []
    rule = 0

    def __init__(self):
        dim = Dimension(900, 450)
        self.setPreferredSize(dim)
        self.setBackground(Color.white)
        self.setFont(Font("SansSerif", Font.BOLD, 28))

        self.cells = [[0] * dim.width for _ in range(dim.height)]
        self.cells[0][dim.width // 2] = 1

        Timer(5000, lambda e: self.update_rule()).start()

    def update_rule(self):
        self.rule = (self.rule + 1) % len(self.ruleSet)
        self.repaint()

    def rules(self, lhs, mid, rhs):
        idx = (lhs << 2 | mid << 1 | rhs)
        return (self.ruleSet[self.rule] >> idx) & 1

    def drawCa(self, g):
        g.setColor(Color.black)
        for r in range(len(self.cells) - 1):
            for c in range(1, len(self.cells[r]) - 1):
                lhs = self.cells[r][c - 1]
                mid = self.cells[r][c]
                rhs = self.cells[r][c + 1]
                self.cells[r + 1][c] = self.rules(lhs, mid, rhs)  # next generation
                if self.cells[r][c] == 1:
                    g.fillRect(c, r, 1, 1)

    def drawLegend(self, g):
        s = str(self.ruleSet[self.rule])
        sw = g.getFontMetrics().stringWidth(s)

        g.setColor(Color.white)
        g.fillRect(16, 5, 55, 30)

        g.setColor(Color.darkGray)
        g.drawString(s, 16 + (55 - sw) // 2, 30)

    def paintComponent(self, gg):
        super().paintComponent(gg)
        g = gg
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON)

        self.drawCa(g)
        self.drawLegend(g)

    def main(args):
        SwingUtilities.invokeLater(lambda: create_and_show_gui())

    def create_and_show_gui():
        f = JFrame()
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        f.setTitle("Wolfram CA")
        f.setResizable(False)
        f.add(WolframCA(), BorderLayout.CENTER)
        f.pack()
        f.setLocationRelativeTo(None)
        f.setVisible(True)