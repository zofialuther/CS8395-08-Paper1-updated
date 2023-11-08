def longest_common_subsequence(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return ""
    elif str1[-1] == str2[-1]:
        return longest_common_subsequence(str1[:-1], str2[:-1]) + str1[-1]
    else:
        lcs1 = longest_common_subsequence(str1, str2[:-1])
        lcs2 = longest_common_subsequence(str1[:-1], str2)
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2