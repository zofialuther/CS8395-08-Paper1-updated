```python
def FifteenPuzzle():
    dim = 640
    margin = 80
    tileSize = (dim - 2 * margin) / 4
    gridSize = tileSize * 4
    setPreferredSize(new Dimension(dim, dim + margin))
    setBackground(Color.WHITE)
    setForeground(new Color(0x6495ED)) # cornflowerblue
    setFont(new Font('SansSerif', Font.BOLD, 60))
    gameOver = True
    addMouseListener(MouseAdapter()):
        mousePressed(MouseEvent e):
            if (gameOver):
                newGame()
            else:
                ex = e.getX() - margin
                ey = e.getY() - margin
                if (ex < 0 or ex > gridSize or ey < 0 or ey > gridSize):
                    return
                c1 = ex // tileSize
                r1 = ey // tileSize
                c2 = blankPos % 4
                r2 = blankPos // 4
                clickPos = r1 * 4 + c1
                dir = 0
                if (c1 == c2 and abs(r1 - r2) > 0):
                    dir = 4 if (r1 - r2) > 0 else -4
                elif (r1 == r2 and abs(c1 - c2) > 0):
                    dir = 1 if (c1 - c2) > 0 else -1
                if (dir != 0):
                    while True:
                        newBlankPos = blankPos + dir
                        tiles[blankPos] = tiles[newBlankPos]
                        blankPos = newBlankPos
                        if blankPos == clickPos:
                            break
                    tiles[blankPos] = 0
                gameOver = isSolved()
            repaint()
        newGame()
    newGame()
    while (not isSolvable()):
        reset()
        shuffle()
        gameOver = False
    reset()
    for i in range(len(tiles)):
        tiles[i] = (i + 1) % len(tiles)
    blankPos = len(tiles) - 1
    shuffle()
    countInversions = 0
    for i in range(15):
        for j in range(i):
            if (tiles[j] > tiles[i]):
                countInversions += 1
    return countInversions % 2 == 0
    isSolved()
    drawGrid(Graphics2D g)
    drawStartMessage(Graphics2D g)
    paintComponent(Graphics gg)
    main(String[] args)
```