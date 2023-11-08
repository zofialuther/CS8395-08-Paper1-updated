def levenshtein(s1, s2):
    if len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)
    else:
        if s1[0] == s2[0]:
            return levenshtein(s1[1:], s2[1:])
        else:
            score1 = levenshtein(s1[1:], s2[1:])
            score2 = levenshtein(s1, s2[1:])
            score3 = levenshtein(s1[1:], s2)
            return 1 + min(score1, score2, score3)

def main():
    print(levenshtein("kitten", "sitting"))

if __name__ == "__main__":
    main()