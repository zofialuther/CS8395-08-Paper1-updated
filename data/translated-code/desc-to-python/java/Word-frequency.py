def printWordFrequency(url):
    import re
    import urllib.request
    from collections import defaultdict

    word_freq = defaultdict(int)
  
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        words = re.findall(r'\b\w+\b', data.lower())
        for word in words:
            word_freq[word] += 1
        sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        for word, freq in sorted_word_freq[:10]:
            print(f'{word}: {freq}')
    except Exception as e:
        print(f'Error: {e}')