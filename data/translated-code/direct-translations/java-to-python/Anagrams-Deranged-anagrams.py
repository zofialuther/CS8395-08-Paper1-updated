from collections import defaultdict
import itertools

def printLongestDerangedAnagram(words):
    words.sort(key=lambda x: (-len(x), x))
    
    anagram_map = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        for anagram in anagram_map[sorted_word]:
            if isDeranged(word, anagram):
                print(anagram, word)
                return
        anagram_map[sorted_word].append(word)
    print("no result")

def isDeranged(word1, word2):
    return all(c1 != c2 for c1, c2 in zip(word1, word2))

if __name__ == "__main__":
    with open("unixdict.txt", "r") as file:
        words = file.read().splitlines()
        printLongestDerangedAnagram(words)