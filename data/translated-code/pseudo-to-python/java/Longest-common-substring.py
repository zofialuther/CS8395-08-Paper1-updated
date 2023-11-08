def lcs(a, b):
    if len(a) > len(b):
        return lcs(b, a)
    
    res = ""
    for ai in range(len(a)):
        for length in range(len(a) - ai, 0, -1):
            for bi in range(len(b) - length + 1):
                if a[ai:ai+length] == b[bi:bi+length] and length > len(res):
                    res = a[ai:ai+length]
    return res

def main():
    print(lcs("testing123testing", "thisisatest"))
    print(lcs("test", "thisisatest"))
    print(lcs("testing", "sting"))
    print(lcs("testing", "thisisasting"))

main()