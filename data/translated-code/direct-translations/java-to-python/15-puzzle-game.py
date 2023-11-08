```python
import pygame
import random

class FifteenPuzzle:
    def __init__(self):
        self.side = 4
        self.numTiles = self.side * self.side - 1
        self.tiles = [0] * (self.numTiles + 1)
        self.tileSize = 160
        self.margin = 80
        self.gridSize = self.tileSize * self.side
        self.gameOver = True

        pygame.init()
        self.screen = pygame.display.set_mode((640, 720))
        pygame.display.set_caption("Fifteen Puzzle")
        self.font = pygame.font.SysFont("SansSerif", 60)

        self.new_game()

    def new_game(self):
        while True:
            self.reset()
            self.shuffle()
            if self.is_solvable():
                self.gameOver = False
                break

    def reset(self):
        for i in range(self.numTiles):
            self.tiles[i] = (i + 1) % self.numTiles
        self.blankPos = self.numTiles

    def shuffle(self):
        n = self.numTiles
        while n > 1:
            r = random.randint(0, n-1)
            self.tiles[r], self.tiles[n-1] = self.tiles[n-1], self.tiles[r]
            n -= 1

    def is_solvable(self):
        countInversions = 0
        for i in range(self.numTiles):
            for j in range(i):
                if self.tiles[j] > self.tiles[i]:
                    countInversions += 1
        return countInversions % 2 == 0

    def is_solved(self):
        if self.tiles[self.numTiles] != 0:
            return False
        for i in range(self.numTiles):
            if self.tiles[i] != i + 1:
                return False
        return True

    def draw_grid(self):
        for i in range(len(self.tiles)):
            r = i // self.side
            c = i % self.side
            x = self.margin + c * self.tileSize
            y = self.margin + r * self.tileSize

            if self.tiles[i] == 0:
                if self.gameOver:
                    pygame.draw.rect(self.screen, (0, 255, 0), (x, y, self.tileSize, self.tileSize))
                    text = self.font.render("\u2713", True, (255, 255, 255))
                    text_rect = text.get_rect(center=(x + self.tileSize // 2, y + self.tileSize // 2))
                    self.screen.blit(text, text_rect)
                continue

            pygame.draw.rect(self.screen, (100, 149, 237), (x, y, self.tileSize, self.tileSize), border_radius=25)
            pygame.draw.rect(self.screen, (0, 0, 139), (x, y, self.tileSize, self.tileSize), border_radius=25, width=3)
            text = self.font.render(str(self.tiles[i]), True, (255, 255, 255))
            text_rect = text.get_rect(center=(x + self.tileSize // 2, y + self.tileSize // 2))
            self.screen.blit(text, text_rect)

    def draw_start_message(self):
        if self.gameOver:
            font = pygame.font.SysFont("SansSerif", 18)
            text = font.render("click to start a new game", True, (100, 149, 237))
            text_rect = text.get_rect(center=(320, 680))
            self.screen.blit(text, text_rect)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.gameOver:
                        self.new_game()
                    else:
                        pos = pygame.mouse.get_pos()
                        ex = pos[0] - self.margin
                        ey = pos[1] - self.margin

                        if ex < 0 or ex > self.gridSize or ey < 0 or ey > self.gridSize:
                            continue

                        c1 = ex // self.tileSize
                        r1 = ey // self.tileSize
                        c2 = self.blankPos % self.side
                        r2 = self.blankPos // self.side

                        clickPos = r1 * self.side + c1

                        dir = 0
                        if c1 == c2 and abs(r1 - r2) > 0:
                            dir = 4 if (r1 - r2) > 0 else -4
                        elif r1 == r2 and abs(c1 - c2) > 0:
                            dir = 1 if (c1 - c2) > 0 else -1

                        if dir != 0:
                            while self.blankPos != clickPos:
                                newBlankPos = self.blankPos + dir
                                self.tiles[self.blankPos] = self.tiles[newBlankPos]
                                self.blankPos = newBlankPos
                            self.tiles[self.blankPos] = 0

                        self.gameOver = self.is_solved()
            self.screen.fill((255, 255, 255))
            self.draw_grid()
            self.draw_start_message()
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = FifteenPuzzle()
    game.run()
```