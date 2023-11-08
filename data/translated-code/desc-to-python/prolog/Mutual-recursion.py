```python
def female(total):
    if total == 0:
        return 1
    else:
        return female(total - 1) - male(total - 1)

def male(total):
    if total == 0:
        return 0
    else:
        return male(total - 1) - female(total - 1)
```