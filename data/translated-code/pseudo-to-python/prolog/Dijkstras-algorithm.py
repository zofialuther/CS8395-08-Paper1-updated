edge = {
    ("a","b"): 7,
    ("a","c"): 9,
    ("b","c"): 10,
    ("b","d"): 15,
    ("c","d"): 11,
    ("d","e"): 6,
    ("a","f"): 14,
    ("c","f"): 2,
    ("e","f"): 9
}

rpath = {}

def path(From, To, Dist):
    if (To, From) in edge:
        return edge[(To, From)]
    elif (From, To) in edge:
        return edge[(From, To)]

def shorterPath(Path, Dist):
    global rpath
    if (Path[0], Path[1]) in rpath:
        if Dist < rpath[(Path[0], Path[1])]:
            del rpath[(Path[0], Path[1])]
            print(f"{Path} is closer than {Path[0], Path[1]}")
            rpath[(Path[0], Path[1])] = Dist
    else:
        print(f"New path: {Path}")
        rpath[(Path[0], Path[1])] = Dist

def traverse(From, Path=[], Dist=0):
    global rpath
    for T in edge:
        if T[0] == From and T[1] not in Path:
            shorterPath([T[1], From] + Path, Dist + edge[T])
            traverse(T[1], [From] + Path, Dist + edge[T])

def go(From, To):
    global rpath
    traverse(From)
    if (To, RPath) in rpath:
        Path = [To] + list(RPath)
        Distance = round(rpath[(To, RPath)])
        print(f"Shortest path is {Path} with distance {rpath[(To, RPath)]} = {Distance}")
    else:
        print(f"There is no route from {From} to {To}")