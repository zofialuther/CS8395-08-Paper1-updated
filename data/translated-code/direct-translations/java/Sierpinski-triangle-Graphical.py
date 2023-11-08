import javax.swing
import java.awt

class SierpinskyTriangle:
    def main(args):
        i = 3  # Default to 3
        if len(args) >= 1:
            try:
                i = int(args[0])
            except ValueError:
                print("Usage: 'java SierpinskyTriangle [level]'\nNow setting level to " + i)
        level = i

        frame = javax.swing.JFrame("Sierpinsky Triangle - Java")
        frame.setDefaultCloseOperation(javax.swing.JFrame.EXIT_ON_CLOSE)

        panel = javax.swing.JPanel():
            def paintComponent(g):
                g.setColor(java.awt.Color.BLACK)
                drawSierpinskyTriangle(level, 20, 20, 360, (java.awt.Graphics2D) g)

        panel.setPreferredSize(java.awt.Dimension(400, 400))

        frame.add(panel)
        frame.pack()
        frame.setResizable(False)
        frame.setLocationRelativeTo(None)
        frame.setVisible(True)

    def drawSierpinskyTriangle(level, x, y, size, g):
        if level <= 0:
            return

        g.drawLine(x, y, x + size, y)
        g.drawLine(x, y, x, y + size)
        g.drawLine(x + size, y, x, y + size)

        drawSierpinskyTriangle(level - 1, x, y, size / 2, g)
        drawSierpinskyTriangle(level - 1, x + size / 2, y, size / 2, g)
        drawSierpinskyTriangle(level - 1, x, y + size / 2, size / 2, g)