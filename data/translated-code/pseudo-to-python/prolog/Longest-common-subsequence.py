string1 = "beginning-middle-ending"
string2 = "beginning-diddle-dum-ending"

def lcs(string1, string2):
    lcsArr = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
    
    for i in range(len(string1) + 1):
        for j in range(len(string2) + 1):
            if i == 0 or j == 0:
                lcsArr[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                lcsArr[i][j] = lcsArr[i-1][j-1] + 1
            else:
                lcsArr[i][j] = max(lcsArr[i-1][j], lcsArr[i][j-1])
    
    i = len(string1)
    j = len(string2)
    lcsString = ""
    
    while i > 0 and j > 0:
        if string1[i-1] == string2[j-1]:
            lcsString = string1[i-1] + lcsString
            i -= 1
            j -= 1
        elif lcsArr[i-1][j] > lcsArr[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return lcsString

Lcs = lcs(string1, string2)
print(Lcs)