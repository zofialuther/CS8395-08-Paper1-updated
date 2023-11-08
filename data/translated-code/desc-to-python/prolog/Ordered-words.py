import urllib.request

# Open a URL and read a list of words
with urllib.request.urlopen('http://example.com/words.txt') as response:
   words = response.read().decode('utf-8').split()

# Process and sort the words based on their length
sorted_words = sorted(words, key=len)

# Predicate for sorting a list of pairs
def pair_sort(pair):
    return (len(pair[1]), pair[0])

# Output the sorted list of words
for word in sorted_words:
    print(word)