def main():
    a = [3,2,1,8,9,4,6]
    print("Unsorted: " + arrayToString(a))
    a = pSort(a)
    print("Sorted: " + arrayToString(a))

def pSort(a):
    list = createArrayList()
    permute(a, len(a), list)
    for x in list:
        if isSorted(x):
            return x
    return a

def permute(a, n, list):
    if n == 1:
        b = createArray(len(a))
        copyArray(a, b)
        list.append(b)
        return
    for i in range(n):
        swap(a, i, n-1)
        permute(a, n-1, list)
        swap(a, i, n-1)

def isSorted(a):
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            return False
    return True

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp