# Initialize boolean variables
true_value = True
false_value = False

# Initialize null variable
null_value = None

# Convert string representation of dictionary to actual dictionary
string_dict = '{"foo": 1, "bar": [10, "apples"]}'
data = eval(string_dict)

print(data)