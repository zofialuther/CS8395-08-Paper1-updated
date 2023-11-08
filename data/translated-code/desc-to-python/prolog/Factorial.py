```python
def fact(N, FN):
    def cont_fact(N, Acc, FN):
        if N == 0:
            FN = Acc
        else:
            Acc *= N
            N -= 1
            cont_fact(N, Acc, FN)
    cont_fact(N, 1, FN)
```