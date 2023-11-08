bellTri = [[1]]

def f(xs):
    return (xs[-1], xs)

result = map(lambda x: f(x)[-1], scanl(lambda x, y: x + y, (1, [1])))

bell = list(map(lambda x: x[0], bellTri))

def main():
    print("First 10 rows of Bell's Triangle:")
    mapM_(print, bellTri)
    print("\nFirst 15 Bell numbers:")
    mapM_(print, bell)
    print("\n" + str(bell[49]))