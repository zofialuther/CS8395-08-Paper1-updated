```python
import data.list
import control.monad
import control.arrow
import rosetta.knuthshuffle

blanco = ["  "] * (31 * 31)
cs = [[-15,-14,..15], [-15,-14,..15]]
constraint = lambda x, y: (x <= 15*15) and (10*10 <= y)
# select and randomize all circle points
pts = knuthShuffle([c for c in cs if constraint(sum(map(lambda x: x[0]*x[1], zip(c, c))), sum(map(lambda x: x*x, c)))])
# 'paint' first 100 randomized circle points on canvas
canvas = blanco[:]
for x, y in pts[:100]:
    canvas[31*(x+15)+y+15] = "/ "
# show canvas
for line in ["".join(chunk) for chunk in zip(*[iter(canvas)]*31)]:
    print(line)
```