def mapM_(f, xs):
    for x in xs:
        f(x)

def printList(xs):
    for x in xs:
        print(x)

mapM_(printList, [1, 2, 3, 4, 5])