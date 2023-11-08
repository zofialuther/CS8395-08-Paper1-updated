```python
fruit = {
    1: "apple",
    2: "banana",
    3: "orange"
}

def write_fruit_name(N):
    name = fruit.get(N, "unknown")
    print("The fruit is {}".format(name))

write_fruit_name(2)
```