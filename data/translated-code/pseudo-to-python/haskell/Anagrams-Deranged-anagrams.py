def groupBySig(strings):
    return [(sorted(s), {s}) for s in strings]

def equivs(groups):
    return [list(group) for group in {tuple(sorted(item[0])): [i for s in item[1] for i in s] for item in groups}.values()]

def isDerangement(pair):
    return all(pair[0][i] != pair[1][i] for i in range(len(pair[0])))

def pairs(lst):
    return [(lst[i], lst[j]) for i in range(len(lst)) for j in range(i+1, len(lst))]

def anagrams(strings):
    equiv_words = equivs(groupBySig(strings))
    return [pair for group in equiv_words for pair in pairs(group)]

def maxDerangedAnagram(strings):
    anagram_pairs = anagrams(strings)
    deranged_anagrams = [pair for pair in anagram_pairs if isDerangement(pair)]
    if not deranged_anagrams:
        return None
    else:
        return max(deranged_anagrams, key=lambda x: len(x[0]))

def main():
    with open("unixdict.txt", "r") as file:
        words = [line.strip() for line in file]
    result = maxDerangedAnagram(words)
    if result:
        print("Longest deranged anagrams:", result[0], result[1])
    else:
        print("No deranged anagrams were found.")

main()