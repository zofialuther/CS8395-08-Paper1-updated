def selection_sort(inputList, outputList):
    if not inputList:
        outputList = []
    else:
        H = inputList[0]
        L = inputList[1:]
        H1 = outputList[0]
        L1 = outputList[1:]
        exchange(H, L, H1, L1)
        selection_sort(L1, L2)

def exchange(H, L, H1, L1):
    if not L:
        H1 = H
        L1 = []
    else:
        H2 = min(L)
        if H < H2:
            H1 = H
            L1 = L
        else:
            H1 = H2
            Ind = L.index(H2)
            L1[Ind] = H
            L[Ind] = H1
            L1 = L2