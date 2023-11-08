def seqR(s, idx, result):
    if idx == len(s):
        print(result)
        return
    seqR(s, idx+1, result + s[idx])
    seqR(s, idx+1, result + " ")

def main():
    s = "abc"
    seqR(s, 0, "")

main()