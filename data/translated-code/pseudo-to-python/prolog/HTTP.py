import urllib.request

def http():
    In = urllib.request.urlopen('http://www.rosettacode.org/')
    data = In.read()
    print(data.decode('utf-8'))
    In.close()