```python
def map_name(Name, MappedString):
    if Name[0] == 'A':
        MappedString = "Apple"
    elif Name[0] == 'B':
        MappedString = "Banana"
    elif Name[0] == 'C':
        MappedString = "Cherry"
    else:
        MappedString = "Unknown"

def song(Name):
    MappedString = ""
    map_name(Name, MappedString)
    print("The song for", Name, "is:", MappedString, MappedString, "Bo B" + MappedString)

def test():
    names = ["Anna", "Bob", "Cathy"]
    for name in names:
        song(name)
```