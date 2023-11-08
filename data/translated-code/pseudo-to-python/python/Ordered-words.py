import urllib.request

url = 'http://www.puzzlers.org/pub/wordlists/unixdict.txt'
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')
words = data.split()

ordered = [word for word in words if sorted(word) == list(word)]

maxlen = max(len(word) for word in ordered)

maxorderedwords = [word for word in ordered if len(word) == maxlen]

print(' '.join(maxorderedwords))