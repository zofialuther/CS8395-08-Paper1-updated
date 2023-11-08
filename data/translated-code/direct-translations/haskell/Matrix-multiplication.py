def multiply(us, vs):
    def mult(xs, zs, ys):
        if not zs or not ys:
            return xs
        if not xs:
            return mult(list(map(lambda x: x * ys[0], zs)), zss[1:], ys[1:])
        return mult(list(map(lambda u, v: u + v * ys[0], xs, zs)), zss, ys[1:])
    
    return list(map(lambda u: mult([], vs, u), us))

def main():
    result = multiply([[1, 2], [3, 4]], [[-3, -8, 3], [-2, 1, 4]])
    for row in result:
        print(row)

main()