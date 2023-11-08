```python
# Define predicate g(N,X) to generate the first N elements of Calkin-Wilf sequence
def g(N, X):
    if N == 0:
        return
    else:
        X.append(1)
        g(N-1, X)
        
# Define predicate t(A/B,X) to generate the index of the fraction A/B in Calkin-Wilf sequence
def t(A, B, X):
    if A == 1 and B == 1:
        return 1
    elif A < B:
        return 2 * t(A, B - A, X)
    else:
        return 2 * t(A - B, B, X) + 1

# Example usage:
result = []
g(5, result)
print(result)
print(t(2, 3, result))
```