import Data.List
import Data.Map.Strict

with open("miserables.txt", "r") as file:
    content = file.read()

character_count = dict()
for char in content:
    if char in character_count:
        character_count[char] += 1
    else:
        character_count[char] = 1

sorted_characters = sorted(character_count.items(), key=lambda x: x[1], reverse=True)
for char, count in sorted_characters:
    print(f"{char}: {count}")