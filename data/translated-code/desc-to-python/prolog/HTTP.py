```python
import http.client

conn = http.client.HTTPConnection("www.rosettacode.org")
conn.request("GET", "/")
response = conn.getresponse()
print(response.read())
conn.close()
```