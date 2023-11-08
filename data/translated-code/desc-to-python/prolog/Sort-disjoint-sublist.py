```python
def test_sort_disjoint_sublist():
    assert sort_disjoint_sublist([1, 3, 2, 5, 4], [2, 5]) == [1, 3, 2, 4, 5]
    assert sort_disjoint_sublist([5, 4, 3, 2, 1], [3, 2]) == [5, 4, 2, 3, 1]
    assert sort_disjoint_sublist([1, 2, 3, 4, 5], [6, 7]) == [1, 2, 3, 4, 5]
    assert sort_disjoint_sublist([1, 2, 2, 3, 4], [2, 2]) == [1, 2, 2, 3, 4]
    assert sort_disjoint_sublist([1, 2, 3, 4, 5], [4, 3]) == "Invalid sublist"

def rt():
    test_sort_disjoint_sublist()
```