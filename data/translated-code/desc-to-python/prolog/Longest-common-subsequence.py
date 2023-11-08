```python
import time

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for i in range(m + 1)]
 
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    
    index = L[m][n]
    lcs = [""] * (index + 1)
    lcs[index] = ""
 
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
 
    print("".join(lcs))

start_time = time.process_time()
lcs("beginningmiddleending", "abcdefghijklmno")
end_time = time.process_time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
```