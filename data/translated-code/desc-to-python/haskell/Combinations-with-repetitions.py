```python
def combinationsWithRepetition(k, xs):
    if k == 0:
        return [[]]
    if not xs:
        return []
    result = []
    for x in xs:
        sub_combinations = combinationsWithRepetition(k-1, xs)
        for sub_combination in sub_combinations:
            result.append([x] + sub_combination)
    return result

def main():
    print(combinationsWithRepetition(2, ['a', 'b', 'c']))
    print(combinationsWithRepetition(3, [1, 2]))
    print(combinationsWithRepetition(0, [1, 2, 3]))

if __name__ == "__main__":
    main()
```