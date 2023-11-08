```python
def wheel2357(n):
    W = [2,3,5,7]
    L = [W[i%4] for i in range(n)]
    return L

def factor(n):
    def factor_helper(n, p, c, m, A):
        if n < p*p:
            return A + [(n,m)] if n > 1 else A
        if n % p == 0:
            return factor_helper(n//p, p, c+1, m, A) 
        return factor_helper(n, p+2, 1, m+c, A+[(p,c)]) if p==2 else factor_helper(n, p+2, 1, m+c, A)

    return factor_helper(n, 2, 1, 0, [])

```