def countSubstring(subStr, str):
    count = 0
    loc = str.find(subStr)
    while loc != -1:
        count = count + 1
        loc = str.find(subStr, loc + len(subStr))
    return count

def main(args):
    countSubstring("th", "the three truths")
    countSubstring("abab", "ababababab")
    countSubstring("a*b", "abaabba*bbaba*bbab")