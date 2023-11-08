import urllib.request
from urllib.request import urlopen

def ordered_words():
    url = 'http://www.puzzlers.org/pub/wordlists/unixdict.txt'
    response = urlopen(url)
    data = response.read().decode('utf-8')

    # process the data and implement the rest of the logic here


# you can call the function here if needed
ordered_words()