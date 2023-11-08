```python
import threading

def main(A):
    threads = []
    L = list(A)
    for i in range(len(A)):
        threads.append(threading.Thread(target=primedecomp, args=(A[i],)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    maxminF = L[0][0]
    maxminI = 0
    for i in range(1, len(L)):
        if maxminF <= L[i][0]:
            maxminF = L[i][0]
            maxminI = i
    print(A[maxminI] + ": " + str(L[maxminI]) + "\n")

def primedecomp(n):         # return a list of factors
    F = []
    genfactors(n, F)
    return F

def genfactors(n, F):
    # implementation of factor generation
    pass
```