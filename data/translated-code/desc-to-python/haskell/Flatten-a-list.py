```python
class Entry:
    def __init__(self, value):
        self.value = value

class NestedList:
    def __init__(self, elements):
        self.elements = elements

def flatten(nested_list):
    flattened_list = []
    for element in nested_list.elements:
        if isinstance(element, Entry):
            flattened_list.append(element.value)
        else:
            flattened_list.extend(flatten(element))
    return flattened_list

def example():
    nested_list = NestedList([Entry(1), NestedList([Entry(2), Entry(3)]), Entry(4)])
    return nested_list

def main():
    example_nested_list = example()
    flattened = flatten(example_nested_list)
    print(flattened)

main()
```