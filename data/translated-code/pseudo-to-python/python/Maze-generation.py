from random import shuffle, randrange

def make_maze(w = 16, h = 8):
    vis = [[0 for _ in range(w+1)] for _ in range(h+1)]
    ver = [["|  " for _ in range(w)] for _ in range(h)]
    hor = [["+--" for _ in range(w)] for _ in range(h)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]
        shuffle(d)
        for xx, yy in d:
            if vis[yy][xx] != 0:
                continue
            if xx == x:
                hor[max(y, yy)][x] = "+  "
            if yy == y:
                ver[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = ""
    for a, b in zip(hor, ver):
        s += ''.join(a) + '\n' + ''.join(b) + '\n'
    return s

if __name__ == '__main__':
    print(make_maze())