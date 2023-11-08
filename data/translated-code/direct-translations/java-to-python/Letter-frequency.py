from collections import defaultdict
import json

# Read the JSON file
with open('file.json', 'r') as file:
    data = json.load(file)

# Create a defaultdict to store the data
data_dict = defaultdict(list)

# Populate the defaultdict with the data from the JSON file
for item in data:
    key = item['key']
    value = item['value']
    data_dict[key].append(value)

# Print the defaultdict
for key, value in data_dict.items():
    print(key, value)