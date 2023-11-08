# Create a 2D array of strings
array = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

# Iterate through the elements of the array and print them out
for sub_array in array:
    for element in sub_array:
        print(element, end=" ") # Print the element followed by a space
    print() # Move to the next line after printing all elements in a sub-array