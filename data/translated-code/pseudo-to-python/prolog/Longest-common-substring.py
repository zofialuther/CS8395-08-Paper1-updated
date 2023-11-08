def common_sublist(A, B, M):
    Ma = A + M
    Mb = M + B

def longest_list(L, LongestList, LongestLength, Result):
    if len(L) == 0:
        return LongestList
    else:
        if len(L) >= LongestLength:
            return longest_list(L[1:], L[0], len(L), Result)
        else:
            return longest_list(L[1:], LongestList, LongestLength, Result)

def longest_substring(A, B, Result):
    AChars = list(A)
    BChars = list(B)
    AllSubstrings = []
    for i in range(len(AChars)):
        for j in range(len(BChars)):
            if AChars[i] == BChars[j]:
                common_sublist(AChars[i:], BChars[j:], [])
    LongestSubString = longest_list(AllSubstrings, [], 0, Result)
    Result = ''.join(LongestSubString)