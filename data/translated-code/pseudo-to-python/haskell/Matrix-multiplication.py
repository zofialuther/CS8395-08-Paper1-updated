def multiply(us, vs):
    def mult(xs, ys, zs):
        if not xs:
            return xs
        elif not ys:
            return xs
        elif not zs:
            return mult(list(map(lambda x: x*ys[0], xs)), ys[1:], zs)
        else:
            return mult([(u + v*ys[0]) for u, v in zip(xs, zs[0])], ys[1:], zs[1:])
    
    return mult(us, vs, [])

def main():
    print(multiply([[1, 2], [3, 4]], [[-3, -8, 3], [-2, 1, 4]]))