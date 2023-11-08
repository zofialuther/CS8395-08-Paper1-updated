import itertools
import random

def replaceAt(index, item, lst):
    lst[index] = item
    return lst

blanco = ["  "] * (31*31)
cs = list(itertools.product(range(-15,16), range(-15,16)))
constraint = lambda x, y: x <= 15*15 and 10*10 <= sum(map(lambda z: z[0]*z[1], zip(x, y)))

pts = list(filter(lambda x: constraint(x[0], x[1]), cs))
random.shuffle(pts)

canvas = blanco.copy()
for point in pts[:100]:
    canvas = replaceAt(31*(point[0]+15)+point[1]+15, "/ ", canvas)

for line in [canvas[i:i+31] for i in range(0, len(canvas), 31)]:
    print("".join(line))