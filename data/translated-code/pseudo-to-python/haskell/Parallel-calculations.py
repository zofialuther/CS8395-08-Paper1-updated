def main(A):
    threads = []
    L = list(A)
    for i in range(len(A)):
        threads.append(thread L[i] := primedecomp(A[i]))
    wait(!threads)

    maxminF = L[maxminI := 1][0]
    for i in range(1, len(L)):
        if maxminF <= L[i][0]:
            maxminI = i
    print(A[maxminI] + ": " + str(!L[maxminI]) + " " + "\n")

def primedecomp(n):
    F = []
    F.append(genfactors(n))
    return F

link factors