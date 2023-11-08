from collections import defaultdict

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

anagrams = defaultdict(list)

for i in range(len(states)):
    for j in range(i+1, len(states)):
        combined = states[i] + states[j]
        sorted_combined = ''.join(sorted(combined))
        anagrams[sorted_combined].append((states[i], states[j]))

for key, value in anagrams.items():
    if len(value) > 1:
        print(value)