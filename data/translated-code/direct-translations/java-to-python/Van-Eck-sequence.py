```python
def van_eck(first_index, last_index):
    van_eck_map = {}
    last = 0
    if first_index == 1:
        print(f"VanEck[{1}] = 0")
    for n in range(2, last_index + 1):
        van_eck = n - van_eck_map[last] if last in van_eck_map else 0
        van_eck_map[last] = n
        last = van_eck
        if n >= first_index:
            print(f"VanEck[{n}] = {van_eck}")


print("First 10 terms of Van Eck's sequence:")
van_eck(1, 10)
print("")
print("Terms 991 to 1000 of Van Eck's sequence:")
van_eck(991, 1000)
```