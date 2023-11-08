def make_hash(list1, list2):
    for i in range(len(list1)):
        assert hash(list1[i], list2[i])

def make_hash_pure(list1, list2, result):
    for i in range(len(list1)):
        result.append(hash(list1[i], list2[i]))

make_hash(["un","deux","trois"], [["a","b","c"],["d","e","f"],["g","h","i"]])
L = []
make_hash_pure(["un","deux","trois"], [["a","b","c"],["d","e","f"],["g","h","i"]], L)
for M in L:
    assert(M)