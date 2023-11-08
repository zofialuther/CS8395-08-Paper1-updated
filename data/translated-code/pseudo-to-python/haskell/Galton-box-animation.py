```python
from Data.Map import Map, unionWith, singleton
from Graphics.Gloss import Picture, color, red, black, blue, circleSolid, rectangleUpperSolid, Translate, foldMap
from Control.Monad.Random import evalRandIO, mapM, getRandomRs
from Graphics.Gloss.Interface.IO.Game import simulate, display, white, InWindow

class Ball:
    def __init__(self, position, turns):
        self.position = position
        self.turns = turns

def updateWorld(world):
    nRows, balls, bins = world
    if y < -nRows-5:
        return (nRows, list(map(update, bs)), bins + x)
    else:
        return (nRows, list(map(update, balls)), bins)
    (x, y) = balls[0].position
    bs = balls[1:]
    b = unionWith(lambda x, y: x + y, bins, singleton(x, 1))

def update(ball):
    x, y = ball.position
    turns = ball.turns
    if -nRows <= y and y < 0:
        return Ball((x + turns[0], y - 1), turns[1:])
    else:
        return Ball((x, y - 1), turns)

def drawWorld(world):
    nRows, balls, bins = world
    ballsP = foldMap(lambda pos: trans(pos, circleSolid(10)), [ball.position for ball in balls if ball.position[1] < 3])
    binsP = foldMapWithKey(drawBin, bins)
    pinsP = foldMap(lambda pos: trans(pos, circleSolid(2)), [(2*j-i-1, -i-1) for i in range(1, nRows+1) for j in range(1, i+1)])

def drawBin(x, h):
    return trans((x, -nRows-7), rectangleUpperSolid(20, -h))

def trans(pos, obj):
    x, y = pos
    return Translate(20 * x, 20 * y, obj)

def startSimulation(nRows, balls):
    simulate(display=InWindow("Galton box", (400, 400), (0, 0)), background=white, fps=50, initialState=(nRows, balls, {}), render=drawWorld, step=updateWorld)

def main():
    balls = evalRandIO(mapM(makeBall, range(1, 100)))
    startSimulation(10, balls)

def makeBall(y):
    return Ball((0, y), filter(lambda x: x != 0, getRandomRs(-1, 1)))

main()
```