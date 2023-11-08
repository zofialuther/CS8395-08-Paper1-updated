import java.awt
import java.awt.event
import javax.swing
import javax.swing.Timer

class SierpinskiCarpet(javax.swing.JPanel):
    dim = 513
    margin = 20
    limit = dim

    def __init__(self):
        self.setPreferredSize(java.awt.Dimension(dim + 2 * margin, dim + 2 * margin)
        self.setBackground(java.awt.Color.white)
        self.setForeground(java.awt.Color.orange)

        javax.swing.Timer(2000, (java.awt.event.ActionEvent e) -> {
            limit /= 3
            if (limit <= 3):
                limit = dim
            self.repaint()
        }).start()

    def drawCarpet(self, g: java.awt.Graphics2D, x: int, y: int, size: int):
        if size < limit:
            return
        size /= 3
        for i in range(9):
            if i == 4:
                g.fillRect(x + size, y + size, size, size)
            else:
                self.drawCarpet(g, x + (i % 3) * size, y + (i // 3) * size, size)

    def paintComponent(self, gg: java.awt.Graphics):
        super().paintComponent(gg)
        g = gg
        g.setRenderingHint(java.awt.RenderingHints.KEY_ANTIALIASING, java.awt.RenderingHints.VALUE_ANTIALIAS_ON)
        g.translate(margin, margin)
        self.drawCarpet(g, 0, 0, dim)

    def main(args: list):
        javax.swing.SwingUtilities.invokeLater(() -> {
            f = javax.swing.JFrame()
            f.setDefaultCloseOperation(javax.swing.JFrame.EXIT_ON_CLOSE)
            f.setTitle("Sierpinski Carpet")
            f.setResizable(False)
            f.add(SierpinskiCarpet(), java.awt.BorderLayout.CENTER)
            f.pack()
            f.setLocationRelativeTo(None)
            f.setVisible(True)