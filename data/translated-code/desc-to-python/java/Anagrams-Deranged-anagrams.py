```python
# Python code to find longest pair of deranged anagrams

from collections import defaultdict

# Read list of words from file
with open('words.txt', 'r') as file:
    words = file.read().split()

# Function to check if two words are deranged anagrams
def areDerangedAnagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    return sorted(word1) != sorted(word2)

# Group words with the same sorted character sequence using a defaultdict
wordMap = defaultdict(list)
for word in words:
    sortedWord = ''.join(sorted(word))
    wordMap[sortedWord].append(word)

# Iterate through each group to find deranged anagrams
longestPair = ("", "")
for group in wordMap.values():
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            if areDerangedAnagrams(group[i], group[j]) and len(group[i]) > len(longestPair[0]):
                longestPair = (group[i], group[j])

# Print the longest pair of deranged anagrams found or "no result"
if longestPair == ("", ""):
    print("no result")
else:
    print(longestPair)
```