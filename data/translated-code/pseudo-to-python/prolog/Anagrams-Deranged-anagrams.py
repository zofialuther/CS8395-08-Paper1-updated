from urllib.request import urlopen
import itertools

def longest_deranged_anagram():
    response = urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt')
    words = response.read().decode('utf-8').split('\n')
    response.close()

    sorted_words = sorted(words)
    grouped_words = [(key, list(group)) for key, group in itertools.groupby(sorted_words, lambda x: ''.join(sorted(x)))]
    word_lengths = [(key, [len(w) for w in group]) for key, group in grouped_words]
    sorted_word_lengths = sorted(word_lengths, key=lambda x: (len(x[1]), x[0]), reverse=True)

    for key, lengths in sorted_word_lengths:
        if len(lengths) == 1:
            continue
        for word1 in lengths:
            found_derangement = False
            for word2 in lengths:
                if word1 != word2 and is_derangement(word1, word2):
                    print(f'Longest deranged anagrams: {key} {word1} {word2}')
                    found_derangement = True
                    break
            if found_derangement:
                break

def is_derangement(word1, word2):
    if len(word1) != len(word2):
        return False
    for char1, char2 in zip(word1, word2):
        if char1 == char2:
            return False
    return True

longest_deranged_anagram()