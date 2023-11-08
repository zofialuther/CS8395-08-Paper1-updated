def msort(L):
    if len(L) <= 1:
        return L
    else:
        mid = len(L) // 2
        left = msort(L[:mid])
        right = msort(L[mid:])
        return merge(left, right)

def split(L):
    return L[::2], L[1::2]

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result