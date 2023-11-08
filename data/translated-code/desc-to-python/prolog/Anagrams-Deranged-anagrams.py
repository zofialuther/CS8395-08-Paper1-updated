```python
# Import necessary libraries
import requests
from itertools import permutations

# Function to retrieve word list from URL
def get_word_list(url):
    response = requests.get(url)
    word_list = response.text.split('\n')
    return word_list

# Function to find deranged anagrams
def find_deranged_anagrams(word_list):
    sorted_words = {}
    for word in word_list:
        key = ''.join(sorted(word))
        if len(word) not in sorted_words:
            sorted_words[len(word)] = {}
        if key not in sorted_words[len(word)]:
            sorted_words[len(word)][key] = []
        sorted_words[len(word)][key].append(word)
    
    for length in sorted(sorted_words.keys(), reverse=True):
        for key in sorted(sorted_words[length].keys()):
            if len(sorted_words[length][key]) > 1:
                for pair in permutations(sorted_words[length][key], 2):
                    if pair[0] != pair[1]:
                        is_deranged = True
                        for i in range(len(pair[0])):
                            if pair[0][i] == pair[1][i]:
                                is_deranged = False
                                break
                        if is_deranged:
                            print(pair)

# URL of word list
url = 'https://www.example.com/wordlist.txt'

# Retrieve word list
word_list = get_word_list(url)

# Find and print deranged anagrams
find_deranged_anagrams(word_list)
```