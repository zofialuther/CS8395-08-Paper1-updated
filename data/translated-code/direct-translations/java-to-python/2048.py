```python
import java.awt.*;
import java.awt.event.*;
import java.util.Random;
import javax.swing.*;

class Game2048 extends JPanel:
    
    class State(Enum):
        start, won, running, over

    colorTable = [
        Color(0x701710), Color(0xFFE4C3), Color(0xfff4d3),
        Color(0xffdac3), Color(0xe7b08e), Color(0xe7bf8e),
        Color(0xffc4c3), Color(0xE7948e), Color(0xbe7e56),
        Color(0xbe5e56), Color(0x9c3931), Color(0x701710)]
    
    target = 2048
    highest = 0
    score = 0
    
    gridColor = Color(0xBBADA0)
    emptyColor = Color(0xCDC1B4)
    startColor = Color(0xFFEBCD)
    
    rand = Random()
    tiles = []
    side = 4
    gamestate = State.start
    checkingAvailableMoves = False

    def __init__(self):
        self.setPreferredSize(Dimension(900, 700))
        self.setBackground(Color(0xFAF8EF))
        self.setFont(Font("SansSerif", Font.BOLD, 48))
        self.setFocusable(True)

        self.addMouseListener(MouseAdapter() {
            def mousePressed(self, e):
                self.startGame()
                self.repaint()
        })

        self.addKeyListener(KeyAdapter() {
            def keyPressed(self, e):
                if e.getKeyCode() == KeyEvent.VK_UP:
                    self.moveUp()
                elif e.getKeyCode() == KeyEvent.VK_DOWN:
                    self.moveDown()
                elif e.getKeyCode() == KeyEvent.VK_LEFT:
                    self.moveLeft()
                elif e.getKeyCode() == KeyEvent.VK_RIGHT:
                    self.moveRight()
                self.repaint()
        })

    def paintComponent(self, gg):
        super().paintComponent(gg)
        g = gg
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON)

        self.drawGrid(g)

    def startGame(self):
        if self.gamestate != State.running:
            self.score = 0
            self.highest = 0
            self.gamestate = State.running
            self.tiles = [[None for _ in range(self.side)] for _ in range(self.side)]
            self.addRandomTile()
            self.addRandomTile()

    def drawGrid(self, g):
        g.setColor(self.gridColor)
        g.fillRoundRect(200, 100, 499, 499, 15, 15)

        if self.gamestate == State.running:
            for r in range(self.side):
                for c in range(self.side):
                    if self.tiles[r][c] == None:
                        g.setColor(self.emptyColor)
                        g.fillRoundRect(215 + c * 121, 115 + r * 121, 106, 106, 7, 7)
                    else:
                        self.drawTile(g, r, c)
        else:
            g.setColor(self.startColor)
            g.fillRoundRect(215, 115, 469, 469, 7, 7)

            g.setColor(self.gridColor.darker())
            g.setFont(Font("SansSerif", Font.BOLD, 128))
            g.drawString("2048", 310, 270)

            g.setFont(Font("SansSerif", Font.BOLD, 20))

            if self.gamestate == State.won:
                g.drawString("you made it!", 390, 350)

            elif self.gamestate == State.over:
                g.drawString("game over", 400, 350)

            g.setColor(self.gridColor)
            g.drawString("click to start a new game", 330, 470)
            g.drawString("(use arrow keys to move tiles)", 310, 530)

    def drawTile(self, g, r, c):
        value = self.tiles[r][c].getValue()

        g.setColor(self.colorTable[int(math.log(value) / math.log(2)) + 1])
        g.fillRoundRect(215 + c * 121, 115 + r * 121, 106, 106, 7, 7)
        s = str(value)

        g.setColor(self.colorTable[0] if value < 128 else self.colorTable[1])

        fm = g.getFontMetrics()
        asc = fm.getAscent()
        dec = fm.getDescent()

        x = 215 + c * 121 + (106 - fm.stringWidth(s)) / 2
        y = 115 + r * 121 + (asc + (106 - (asc + dec)) / 2)

        g.drawString(s, x, y)
```