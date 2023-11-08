```python
def maxsumseq(seq):
    max_sum = float('-inf')
    start = 0
    end = 0

    for i in range(len(seq)):
        for j in range(i, len(seq)):
            current_sum = sum(seq[i:j+1])
            if current_sum > max_sum:
                max_sum = current_sum
                start = i
                end = j

    return seq[start:end+1]

# Assertions
assert maxsumseq([1, -3, 4, -2, -1, 6]) == [4, -2, -1, 6]
assert sum(maxsumseq([1, -3, 4, -2, -1, 6])) == max(sum([1, -3, 4, -2, -1, 6]), 0)
assert sum(maxsumseq([1, -3, 4, -2, -1, 6])) == max(sum([1, -3, 4, -2, -1, 6]), 0)
```