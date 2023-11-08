states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

def solve(input):
    orig = {i.replace(" ", "").lower(): i for i in input}
    keys = list(orig.keys())
    map = {}
    for i in input:
        for j in input:
            if i != j:
                pair = [i, j]
                key = "".join(sorted(pair[0] + pair[1]))
                if key not in map:
                    map[key] = []
                map[key].append(pair)
    
    for key in map:
        for pair in map[key]:
            if len(set(pair)) < 4:
                print(pair[0] + " - " + pair[1])

solve(states)