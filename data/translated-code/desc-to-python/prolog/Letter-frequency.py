```python
def packList(lst):
    packed = []
    if len(lst) == 0:
        return packed
    else:
        subList = [lst[0]]
        for i in range(1, len(lst)):
            if lst[i] == subList[0]:
                subList.append(lst[i])
            else:
                packed.append(subList)
                subList = [lst[i]]
        packed.append(subList)
        return packed

with open("file.txt", "r") as file:
    text = file.read()
    characters = list(map(ord, text))
    alphabetic_chars = [chr(char).upper() for char in characters if chr(char).isalpha()]
    sorted_chars = sorted(alphabetic_chars)
    packed_list = packList(sorted_chars)
    frequency = [(sublist[0], len(sublist)) for sublist in packed_list]
    for char, freq in frequency:
        print(f"Character {char} occurs {freq} times")
```