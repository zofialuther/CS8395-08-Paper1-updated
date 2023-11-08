```python
def a_to_z(From, To, L):
    C_From = [ord(c) for c in From]
    C_To = [ord(c) for c in To]
    L1 = [chr(i) for i in range(min(C_From), max(C_To) + 1)]
    L = L1
```