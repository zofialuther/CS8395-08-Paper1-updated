import itertools

n = 20

pythagorean_triplets = [(x, y, z) for x in range(1, n+1) for y in range(1, n+1) for z in range(1, n+1) if x**2 + y**2 == z**2]

pythagorean_triplets_generator = ((x, y, z) for x in range(1, n+1) for y in range(1, n+1) for z in range(1, n+1) if x**2 + y**2 == z**2)

def triplets(n):
    for x, y, z in itertools.product(range(1, n+1), repeat=3):
        if x**2 + y**2 == z**2:
            yield (x, y, z)

pythagorean_triplets_with_generator = [triplet for triplet in triplets(n)]

iterator = triplets(n)

def pts(n):
    return [(x, y, z) for x in range(1, n+1) for y in range(1, n+1) for z in range(1, n+1) if x**2 + y**2 == z**2]

bindList = lambda f, xs: [x for x in xs for x in f]

concatMap = lambda f, xs: [y for ys in [f(x) for x in xs] for y in ys]

def pts2(n):
    return bindList(lambda x: bindList(lambda y: bindList(lambda z: [(x, y, z)], range(1, n+1)), range(1, n+1)), range(1, n+1))

def pts3(n):
    return concatMap(lambda x: concatMap(lambda y: concatMap(lambda z: [(x, y, z)], range(1, n+1)), range(1, n+1)), range(1, n+1))

def main():
    print(pts(20))
    print(pts2(20))
    print(pts3(20))

main()