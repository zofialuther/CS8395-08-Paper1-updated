```python
def consolidated(pairs):
    def merge(result, pair):
        if not result or result[-1][1] < pair[0]:
            result.append(pair)
        else:
            result[-1] = (result[-1][0], max(result[-1][1], pair[1]))
        return result
    return sorted(reduce(merge, pairs, []))

def tabulated(data):
    for d in data:
        print(d)

def showPairs(pairs):
    for pair in pairs:
        print(pair)

def showPair(pair):
    print(pair)

def showNum(num):
    print(num)

def main():
    pairs = [(1.0, 3.0), (2.0, 4.0), (5.0, 7.0), (6.0, 8.0)]
    consolidated_pairs = consolidated(pairs)
    tabulated(consolidated_pairs)

if __name__ == "__main__":
    main()
```