def main():
    treeList = a(a(1), 2, a(a(3, 4), 5), a(a(a())), a(a(a(6))), 7, 8, a())
    flatList = FlattenUtil.flatten(treeList)
    print(treeList)
    print("flatten: " + flatList)

def a(a):
    return list(a)