def levenshtein(s1, s2):
    if len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)
    elif s1[0] == s2[0]:
        return levenshtein(s1[1:], s2[1:])
    else:
        return 1 + min(levenshtein(s1, s2[1:]), levenshtein(s1[1:], s2), levenshtein(s1[1:], s2[1:]))

def main():
    result = levenshtein("kitten", "sitting")
    print(result)

main()