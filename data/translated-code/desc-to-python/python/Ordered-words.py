import urllib.request

url = "https://www.example.com/wordlist.txt"
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')
word_list = text.split()

ordered_words = []
for word in word_list:
    if sorted(word) == list(word):
        ordered_words.append(word)

longest_length = max(len(word) for word in ordered_words)
longest_ordered_words = [word for word in ordered_words if len(word) == longest_length]

print(longest_ordered_words)