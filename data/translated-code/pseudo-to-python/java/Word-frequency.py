def printWordFrequency():
    import urllib.request
    import re
    from collections import defaultdict
    url = "https://www.gutenberg.org/files/135/135-0.txt"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            words = re.findall(r'\w+', data.lower())
            word_count = defaultdict(int)
            for word in words:
                word_count[word] += 1
            sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
            count = 1
            for word, frequency in sorted_word_count:
                print(word, frequency)
                if count == 10:
                    break
                count += 1
    except:
        print("Error reading URL")