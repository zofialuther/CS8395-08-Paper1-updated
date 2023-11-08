```python
import java.awt.*
import java.awt.event.*
import java.util.Random
import javax.swing.*

class Game2048(JPanel):
    class State(Enum):
        start, won, running, over

    colorTable = [Color(0x701710), Color(0xFFE4C3), Color(0xfff4d3), Color(0xffdac3), Color(0xe7b08e), Color(0xe7bf8e), Color(0xffc4c3), Color(0xE7948e), Color(0xbe7e56), Color(0xbe5e56), Color(0x9c3931), Color(0x701710)]

    target = 2048
    highest = 0
    score = 0

    gridColor = Color
    emptyColor = Color
    startColor = Color

    rand = Random
    tiles = []
    side = 4
    gamestate = State
    checkingAvailableMoves = bool

    def Game2048(self):
        self.setPreferredSize(Dimension(900, 700))
        self.setBackground(Color(0xFAF8EF))
        self.setFont(Font("SansSerif", Font.BOLD, 48))
        self.setFocusable(True)

        self.addMouseListener(MouseListener):
            def mousePressed(self, e):
                self.startGame()
                self.repaint()

        self.addKeyListener(KeyListener):
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

    def paintComponent(self, gg):
        super().paintComponent(gg)
        g = gg.create()
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON)
        self.drawGrid(g)

    def startGame(self):
        if self.gamestate != self.State.running:
            self.score = 0
            self.highest = 0
            self.gamestate = self.State.running
            self.tiles = [[Tile() for _ in range(self.side)] for _ in range(self.side)]
            self.addRandomTile()
            self.addRandomTile()

    def drawGrid(self, g):
        # [Drawing grid and tiles]

    def addRandomTile(self):
        # [Logic for adding a random tile]

    def move(self, countDownFrom, yIncr, xIncr):
        # [Logic for moving tiles]

    def moveUp(self):
        return self.move(0, -1, 0)

    def moveDown(self):
        return self.move(self.side * self.side - 1, 1, 0)

    def moveLeft(self):
        return self.move(0, 0, -1)

    def moveRight(self):
        return self.move(self.side * self.side - 1, 0, 1)

    def clearMerged(self):
        # [Logic for clearing merged tiles]

    def movesAvailable(self):
        # [Logic for checking available moves]

    def main(args):
        SwingUtilities.invokeLater(() -> {
            f = JFrame()
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
            f.setTitle("2048")
            f.setResizable(True)
            f.add(Game2048(), BorderLayout.CENTER)
            f.pack()
            f.setLocationRelativeTo(None)
            f.setVisible(True)

class Tile:
    # [Implementation of Tile class]
```