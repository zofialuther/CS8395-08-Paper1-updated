def insertion_sort(a):
    for i in range(1, len(a)):
        j = abs(binary_search(a[:i], a[i])) + 1
        a[j:i+1] = rotate(a[j:i+1], j - i)

def insertion_sort_array(a):
    for i in range(1, len(a)):
        x = a[i]
        j = abs(binary_search_array(a, 0, i, x)) + 1
        a[j+1:i+1] = a[j:i]
        a[j] = x