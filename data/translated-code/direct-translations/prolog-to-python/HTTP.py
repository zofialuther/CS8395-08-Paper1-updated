import urllib.request

def http():
    with urllib.request.urlopen('http://www.rosettacode.org/') as response:
        html = response.read()
        print(html.decode('utf-8'))

http()