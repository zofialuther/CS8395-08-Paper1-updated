import requests

url = "https://www.rosettacode.org"
response = requests.get(url)
print(response.text)