```python
def shuffle_list(strings):
    # function to shuffle the list of strings
    pass

def compare_strings(original, shuffled):
    # function to compare original and shuffled strings
    pass

def calculate_score(string):
    # function to calculate the minimum value based on the quantity of letters in the string
    pass

def sort_and_pack(letters):
    # function to sort and pack the list of letters
    pass

# main program
strings = ["string1", "string2", "string3"]
shuffled_list = shuffle_list(strings)
best_shuffle = ""
best_score = float('inf')

for s in shuffled_list:
    score = calculate_score(s)
    if score < best_score:
        best_shuffle = s
        best_score = score

original_string = strings[shuffled_list.index(best_shuffle)]
sorted_letters = sort_and_pack(list(best_shuffle))

print("Best Shuffle:", best_shuffle)
print("Original String:", original_string)
print("Score:", best_score)
```