from collections import defaultdict
from functools import reduce

def hashJoin(xs, fx, ys, fy):
    l = []
    ht = defaultdict(list)
    for y in ys:
        ht[fy(y)].append(y)
    for x in xs:
        if fx(x) in ht:
            l.extend([(x, v) for v in ht[fx(x)]])
    return l

def main():
    result = hashJoin([(1, "Jonah"), (2, "Alan"), (3, "Glory"), (4, "Popeye")], lambda x: x[1], [("Jonah", "Whales"), ("Jonah", "Spiders"), ("Alan", "Ghosts"), ("Alan", "Zombies"), ("Glory", "Buffy")], lambda x: x[0])
    for item in result:
        print(item)

main()