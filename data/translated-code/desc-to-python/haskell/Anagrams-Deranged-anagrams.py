```python
def read_words_from_file(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
    return words

def group_words_by_sorted_characters(words):
    grouped_words = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in grouped_words:
            grouped_words[sorted_word].append(word)
        else:
            grouped_words[sorted_word] = [word]
    return grouped_words

def find_anagrams(grouped_words):
    anagrams = []
    for key in grouped_words:
        if len(grouped_words[key]) > 1:
            anagrams.append(grouped_words[key])
    return anagrams

def find_longest_deranged_anagram(anagrams):
    deranged_anagrams = []
    for anagram_set in anagrams:
        for i in range(len(anagram_set)):
            for j in range(i+1, len(anagram_set)):
                if is_deranged_anagram(anagram_set[i], anagram_set[j]):
                    deranged_anagrams.append((anagram_set[i], anagram_set[j]))
    if deranged_anagrams:
        return max(deranged_anagrams, key=lambda x: len(x[0]))
    else:
        return "No deranged anagrams found."

def is_deranged_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    for char in word1:
        if word1.count(char) != word2.count(char):
            return True
    return False

file_name = 'words.txt'
words = read_words_from_file(file_name)
grouped_words = group_words_by_sorted_characters(words)
anagrams = find_anagrams(grouped_words)
longest_deranged_anagram = find_longest_deranged_anagram(anagrams)
print(longest_deranged_anagram)
```