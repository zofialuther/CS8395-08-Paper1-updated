```python
def search_a_list(N1, N2, L):
    print("List of names:", L)
    
    if N1 in L:
        print(N1, "is present at position", L.index(N1))
        print("Last position of", N1, "is", len(L) - L[::-1].index(N1))
    else:
        print(N1, "is not present in the list")
    
    if N2 in L:
        print(N2, "is present at position", L.index(N2))
    else:
        print(N2, "is not present in the list")

search_a_list("John", "Alice", ["Tom", "Alice", "John", "Bob", "Alice"])
```