```python
def foldr(Foldy, Items, Starter):
    if not Items:
        return Starter
    else:
        return Foldy(Items[0], foldr(Foldy, Items[1:], Starter))
```