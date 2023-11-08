```python
def huffman():
    L = 'this is an example for huffman encoding'
    LA = list(L)
    LS = sorted(LA)
    PL = packList(LS)
    PLS = sorted(PL)
    A = build_tree(PLS)
    C = coding(A, [])
    SC = sorted(C)
    print('Symbol\tWeight\t\t\t\t\tCode\n')
    for code in SC:
        print_code(code)

def build_tree(nodes):
    if len(nodes) == 1:
        return nodes[0]
    else:
        V1, R1 = nodes[0]
        V2, R2 = nodes[1]
        V = V1 + V2
        A = [V, [V1, R1], [V2, R2]]
        if len(nodes) == 2:
            return A
        else:
            NT = sorted([A] + nodes[2:])
            return build_tree(NT)

def coding(tree, code):
    if is_node(tree[1]):
        C1 = coding(tree[1], [0] + code)
    else:
        C1 = leaf_coding(tree[1], [0] + code)
    if is_node(tree[2]):
        C2 = coding(tree[2], [1] + code)
    else:
        C2 = leaf_coding(tree[2], [1] + code)
    return C1 + C2

def leaf_coding(tree, code):
    codeR = code[::-1]
    return [[tree[1], tree[2], codeR]]

def is_node(node):
    return isinstance(node, list)

def print_code(code):
    N, Car, Code = code
    print(f'{Car}:\t{N}\t\t\t\t{"".join(map(str, Code))}\n')

def packList(lst):
    packed = []
    while lst:
        x = lst[0]
        count = lst.count(x)
        packed.append([count, x])
        lst = [el for el in lst if el != x]
    return packed
```