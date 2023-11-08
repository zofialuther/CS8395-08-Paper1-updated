```python
def ascii():
    for i in range(32, 127):
        row(i)

def row(code):
    print(f"{code} : {chr(code)}")

ascii()
```