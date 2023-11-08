```python
import string

def puzzle(states):
    def pkey(state):
        return ''.join(sorted(filter(str.isalpha, state.lower())))

    def is_valid(pair):
        ((a0, a1), (b0, b1)) = pair
        return a0 != b0 and a0 != b1 and a1 != b0 and a1 != b1

    def pairs(lst):
        return [(lst[i], lst[j]) for i in range(len(lst)) for j in range(i+1, len(lst))]

    sorted_states = sorted(set(states))
    pairs_list = pairs(sorted_states)
    grouped_pairs = [list(g) for _, g in groupby(sorted(pairs_list), key=lambda x: x[0])]
    filtered_pairs = filter(lambda x: len(x) > 1, grouped_pairs)
    valid_pairs = filter(lambda x: is_valid(x), concatMap(lambda x: pairs(x), map(lambda x: x[1], filtered_pairs)))
    return list(valid_pairs)

state_names = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", 
    "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", 
    "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", 
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", 
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", 
    "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

fake_state_names = [
    "New Kory", "Wen Kory", "York New", "Kory New", "New Kory"
]

print(puzzle(state_names + fake_state_names))
```