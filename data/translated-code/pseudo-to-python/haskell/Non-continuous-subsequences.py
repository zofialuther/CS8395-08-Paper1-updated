```python
def disjoint(a):
    def cutAt(s, n):
        left = s[:n]
        right = s[n:]
        right = [x for x in right if x != []]
        return [(left, b) for b in right]

    result = [cutAt(a, n) for n in range(1, len(a) - 1)]
    return [item for sublist in result for item in sublist]

def main():
    print(len(disjoint(list(range(1, 21))))

main()
```