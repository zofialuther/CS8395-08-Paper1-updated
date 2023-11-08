```python
# Python code to solve US state anagram puzzle

# List of US state names
us_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

# Create a map of the original state names, remove spaces and convert to lowercase
state_map = {state: ''.join(state.split()).lower() for state in us_states}

# Iterate through the list of state names, create pairs of states, and check for anagrams
anagram_pairs = []
for i in range(len(us_states)):
    for j in range(i+1, len(us_states)):
        key1 = ''.join(sorted(state_map[us_states[i]]))
        key2 = ''.join(sorted(state_map[us_states[j]]))
        if key1 == key2:
            anagram_pairs.append((us_states[i], us_states[j]))

# Print out the pairs of states that form anagrams
for pair in anagram_pairs:
    print(pair)
```