class NestedList:
    def __init__(self, value):
        self.value = value
        self.entries = []

def flatten(nl):
    result = []
    stack = [nl]
    while stack:
        current = stack.pop()
        if isinstance(current.value, int):
            result.append(current.value)
        else:
            for entry in current.entries:
                stack.append(entry)
    return result

example = NestedList(None)
example.entries = [NestedList(1), 2, NestedList([NestedList(3), NestedList(4), 5]), NestedList([NestedList([])]), NestedList([NestedList([NestedList(6)]), 7, 8, NestedList([])])]

print(flatten(example))
# output [1, 2, 3, 4, 5, 6, 7, 8]