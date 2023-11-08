needles = [1, 2, 3]
haystack = [1, 2, 3, 4, 5]

def find_indices(x):
    return (x, [i for i in range(len(haystack)) if haystack[i] == x])

result = map(find_indices, needles)
print(list(result))