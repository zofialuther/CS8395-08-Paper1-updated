def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    LCSuff = [[0] * (n + 1) for i in range(m + 1)]
    result = 0
    end = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                LCSuff[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                if LCSuff[i][j] > result:
                    result = LCSuff[i][j]
                    end = i - 1
            else:
                LCSuff[i][j] = 0
    return str1[end - result + 1: end + 1]

# Testing the lcs function
print(lcs("abcdef", "abc"))
print(lcs("abcdef", "xyzabcde"))
print(lcs("apple", "banana"))