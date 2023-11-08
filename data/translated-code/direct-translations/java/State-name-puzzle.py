```python
states = ["Alabama", "Alaska", "Arizona", "Arkansas",
        "California", "Colorado", "Connecticut", "Delaware", "Florida",
        "Georgia", "hawaii", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
        "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",
        "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
        "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
        "New York", "North Carolina ", "North Dakota", "Ohio", "Oklahoma",
        "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
        "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
        "Washington", "West Virginia", "Wisconsin", "Wyoming",
        "New Kory", "Wen Kory", "York New", "Kory New", "New Kory"]

def solve(input):
    orig = {s.replace(" ", "").lower(): s for s in input}
    input = list(orig.keys())
    
    map = {}
    for i in range(len(input) - 1):
        pair0 = input[i]
        for j in range(i + 1, len(input)):
            pair = [pair0, input[j]]
            s = pair0 + pair[1]
            key = ''.join(sorted(s))
            val = map.get(key, [])
            val.append(pair)
            map[key] = val
    
    for key, lst in map.items():
        for i in range(len(lst) - 1):
            a = lst[i]
            for j in range(i + 1, len(lst)):
                b = lst[j]
                if len(set(a + b)) < 4:
                    continue
                print(f"{orig[a[0]]} + {orig[a[1]]} = {orig[b[0]]} + {orig[b[1]]}")

solve(states)
```