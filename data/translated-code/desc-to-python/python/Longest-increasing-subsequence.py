```python
def longest_increasing_subsequence(d):
    n = len(d)
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if d[i] > d[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    max_length = max(lis)
    max_index = lis.index(max_length)
    result = [d[max_index]]
    for i in range(max_index - 1, -1, -1):
        if d[i] < d[max_index] and lis[i] == lis[max_index] - 1:
            result.append(d[i])
            max_index = i
    return result[::-1]

input1 = [3, 4, -1, 0, 6, 2, 3]
input2 = [5, 6, 7, 8, 1, 2, 3, 9]

print(longest_increasing_subsequence(input1))
print(longest_increasing_subsequence(input2))
```