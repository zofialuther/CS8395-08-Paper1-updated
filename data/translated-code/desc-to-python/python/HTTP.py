import requests

response = requests.get("http://rosettacode.org")
print(response.text)