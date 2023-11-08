from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class HTree:
    value: str
    code: str
    left: 'HTree' = None
    right: 'HTree' = None

def serialize(tree: HTree) -> List[Tuple[str, str]]:
    if tree.left and tree.right:
        return [(x, '0' + y) for x, y in serialize(tree.left)] + [(x, '1' + y) for x, y in serialize(tree.right)]
    else:
        return [(tree.value, tree.code)]

def huffmanTree(freq: List[Tuple[int, str]]) -> HTree:
    nodes = [HTree(value=str(x), code='', left=None, right=None) for _, x in freq]
    while len(nodes) > 1:
        left = nodes.pop(0)
        right = nodes.pop(0)
        new_node = HTree(value='', code='', left=left, right=right)
        nodes.append(HTree(value='', code='', left=left, right=right))
        nodes.sort(key=lambda x: x.value)
    return nodes[0]

def freq(data: str) -> List[Tuple[int, str]]:
    sorted_data = sorted(data)
    grouped_data = [(len(list(g)), k) for k, g in groupby(sorted_data)]
    return sorted(grouped_data, key=lambda x: x[1])

def test(data: str) -> None:
    freq_data = freq(data)
    huffman_tree = huffmanTree(freq_data)
    serialized_data = serialize(huffman_tree)
    for pair in serialized_data:
        print(f"'{pair[0]} : {pair[1]}'")

if __name__ == "__main__":
    test("this is an example for huffman encoding")