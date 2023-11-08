```python
def common_sublist(A, B, M):
    for i in range(len(A)):
        for j in range(len(A), i, -1):
            if A[i:j] in B and len(A[i:j]) > len(M):
                M = A[i:j]
    return M

def longest_list(L, LongestList, LongestLength, Result):
    if not L:
        return Result
    else:
        if len(L[0]) >= LongestLength:
            return longest_list(L[1:], L[0], len(L[0]), L[0])
        else:
            return longest_list(L[1:], LongestList, LongestLength, Result)

def longest_substring(A, B):
    AChars = list(A)
    BChars = list(B)
    AllSubstrings = [common_sublist(AChars, BChars, []) for _ in range(len(AChars)) for _ in range(len(BChars))]
    LongestSubString = longest_list(AllSubstrings, [], 0, [])
    return ''.join(LongestSubString)
```