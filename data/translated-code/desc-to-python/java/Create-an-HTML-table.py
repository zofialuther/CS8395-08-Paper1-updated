```python
# Create a simple HTML table
html = "<table border='1'>"
html += "<tr><th>X</th><th>Y</th><th>Z</th></tr>"

# Add four rows of numerical values
for i in range(1, 5):
    html += f"<tr><td>{i}</td><td>{i*2}</td><td>{i*3}</td></tr>"

html += "</table>"

print(html)
```