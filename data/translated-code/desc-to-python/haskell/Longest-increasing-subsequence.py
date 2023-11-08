```python
from itertools import combinations

def lis(arr):
    subs = [list(comb) for i in range(len(arr)) for comb in combinations(arr, i+1)]
    sorted_subs = [sub for sub in subs if sub == sorted(sub)]
    unique_subs = [list(sub) for sub in set(map(tuple, sorted_subs))]
    longest_sub = max(unique_subs, key=len)
    return longest_sub

def main():
    input_lists = [[3, 4, -1, 0, 6, 2, 3], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
    for arr in input_lists:
        print(f"The longest increasing subsequence for {arr} is {lis(arr)}")

if __name__ == "__main__":
    main()
```